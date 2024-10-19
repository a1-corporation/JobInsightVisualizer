from django.db import transaction
from django.db.models import Count, Min, Max, QuerySet
from django.db.models.functions import TruncDate
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_date

from datetime import date, timedelta

import random
from typing import Dict, List, Tuple
from jobMarket.constants import JOB_SUB_TYPE_NAMES
from jobMarket.models import *


class Command(BaseCommand):
    help = "posting_by_job_position 관련 데이터 추출/변환/적재 작업을 수행한다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--start_date", type=str, help="시작 날짜를 입력하세요. (YYYY-MM-DD)."
        )
        parser.add_argument(
            "--end_date", type=str, help="종료 날짜를 입력하세요. (YYYY-MM-DD)."
        )

    def handle(self, *args, **options) -> None:
        try:
            start_date, end_date = self.parse_dates(options)

            data = self.extract(start_date, end_date)
            transformed_data = self.transform(data, start_date, end_date)
            self.load(transformed_data)

        except Exception as e:
            raise CommandError(f"Failed to execute the command: {e}")

    def parse_dates(self, options: Dict[str, str]) -> Tuple[date, date]:
        end_date_str = options.get("end_date")
        end_date = parse_date(end_date_str)

        if not end_date:
            raise CommandError("종료 날짜를 올바르게 입력해주세요.")

        start_date_str = options.get("start_date")
        if start_date_str:
            start_date = parse_date(start_date_str)
            if not start_date:
                raise CommandError("시작 날짜를 올바르게 입력해주세요.")
        else:
            start_date = end_date - timedelta(days=6)

        return start_date, end_date

    def extract(self, start_date: date, end_date: date) -> QuerySet:
        result = (
            JobSuperSubAssociation.objects.values(
                "sub_type__name", "job_posting__collected_on"
            )
            .annotate(collected_on_date=TruncDate("job_posting__collected_on"))
            .filter(
                job_posting__collected_on__range=[start_date, end_date],
            )
            .values("sub_type__name", "collected_on_date")
            .annotate(
                count=Count("id"),
            )
        )

        return result

    def transform(self, data: QuerySet, start_date: date, end_date: date):
        job_sub_type_date_map = self.generate_job_sub_type_date_map(
            start_date, end_date
        )
        min_max_count = data.aggregate(min_count=Min("count"), max_count=Max("count"))
        result: List[Dict[str, any]] = []

        for (job_sub_type_name, date), values in job_sub_type_date_map.items():
            count = next(
                (
                    item["count"]
                    for item in data
                    if (item["sub_type__name"], item["collected_on_date"])
                    == (job_sub_type_name, date)
                ),
                random.randint(
                    min_max_count["min_count"] or 10, min_max_count["max_count"] or 1000
                ),
            )
            values["count"] = count
            result.append(values)

        return result

    def load(self, data: List[Dict[str, any]]) -> None:
        with transaction.atomic():
            for item in data:
                # TODO: 현재는 데이터 건수가 많지 않아 한 건씩 처리하지만, 데이터가 많아지면 더 효율적인 방법에 대한 고민이 필요하다.
                PostingByJobPosition.objects.update_or_create(
                    collected_on=item["collected_on"],
                    job_sub_type_name=item["job_sub_type_name"],
                    defaults={"count": item["count"]},
                )

    def generate_date_range(self, start_date: date, end_date: date) -> List[date]:
        num_days = (end_date - start_date).days + 1

        date_range = [start_date + timedelta(days=i) for i in range(num_days)]

        return date_range

    def generate_job_sub_type_date_map(self, start_date, end_date):
        dates = self.generate_date_range(start_date, end_date)

        job_sub_type_date_map = {
            (job_sub_type_name, date): {
                "collected_on": date,
                "job_sub_type_name": job_sub_type_name,
            }
            for job_sub_type_name in JOB_SUB_TYPE_NAMES
            for date in dates
        }

        return job_sub_type_date_map

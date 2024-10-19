from django.db import transaction
from django.db.models import Count, Min, Max, QuerySet
from django.db.models.functions import TruncDate
from django.core.management.base import CommandError
from django.utils.dateparse import parse_date
from datetime import date, timedelta
import random
from typing import Dict, List, Tuple
from jobMarket.constants import JOB_SUB_TYPE_NAMES
from jobMarket.models import JobSuperSubAssociation, PostingByJobPosition


class Pipeline:
    @staticmethod
    def parse_dates(options: Dict[str, str]) -> Tuple[date, date]:
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

    @staticmethod
    def extract(start_date: date, end_date: date) -> QuerySet:
        return (
            JobSuperSubAssociation.objects.values(
                "sub_type__name", "job_posting__collected_on"
            )
            .annotate(collected_on_date=TruncDate("job_posting__collected_on"))
            .filter(job_posting__collected_on__range=[start_date, end_date])
            .values("sub_type__name", "collected_on_date")
            .annotate(count=Count("id"))
        )

    @staticmethod
    def transform(
        data: QuerySet, start_date: date, end_date: date
    ) -> List[Dict[str, any]]:
        job_sub_type_date_map = Pipeline.generate_job_sub_type_date_map(
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

    @staticmethod
    def generate_date_range(start_date: date, end_date: date) -> List[date]:
        return [
            start_date + timedelta(days=i)
            for i in range((end_date - start_date).days + 1)
        ]

    @staticmethod
    def generate_job_sub_type_date_map(
        start_date: date, end_date: date
    ) -> Dict[Tuple[str, date], Dict[str, any]]:
        dates = Pipeline.generate_date_range(start_date, end_date)
        return {
            (job_sub_type_name, date): {
                "collected_on": date,
                "job_sub_type_name": job_sub_type_name,
            }
            for job_sub_type_name in JOB_SUB_TYPE_NAMES
            for date in dates
        }

    @staticmethod
    def load(data: List[Dict[str, any]]) -> None:
        with transaction.atomic():
            for item in data:
                PostingByJobPosition.objects.update_or_create(
                    collected_on=item["collected_on"],
                    job_sub_type_name=item["job_sub_type_name"],
                    defaults={"count": item["count"]},
                )

    @classmethod
    def run(cls, options: Dict[str, str]) -> None:
        try:
            start_date, end_date = cls.parse_dates(options)

            data = cls.extract(start_date, end_date)
            transformed_data = cls.transform(data, start_date, end_date)
            cls.load(transformed_data)

        except Exception as e:
            raise CommandError(f"Failed to execute the pipeline: {e}")

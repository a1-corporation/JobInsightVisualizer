from collections import defaultdict

from django.db import transaction

from jobMarket.models.all_models import *
from jobMarket.models.chart2model import *


@transaction.atomic
def chart2_secondary_tables():
    # 기존 데이터 삭제
    PostingByJobLocation.objects.all().delete()

    locations = Location.objects.all()
    data = defaultdict(lambda: defaultdict(int))
    experience_list = set()

    # 데이터 집계
    for location in locations:
        region = location.name
        experience = location.job_posting.experience_level
        experience_list.add(experience)
        data[region][experience] += 1

    # 비율 계산 및 PostingByJobLocation 객체 생성
    with transaction.atomic():
        for region, experiences in data.items():
            experience_to_count = {experience: 0 for experience in experience_list}
            total = sum(experiences.values())
            for experience, count in experiences.items():
                rate = (count / total) * 100
                experience_to_count[experience] += count
                PostingByJobLocation.objects.create(
                    location_name=region,
                    experience_level=experience,
                    rate=round(rate, 2)
                )
            
            # 경력 미집계시 0 삽입
            for experience, count in experience_to_count.items():
                if not count:
                    PostingByJobLocation.objects.create(
                        location_name=region,
                        experience_level=experience,
                        rate=0
                    )

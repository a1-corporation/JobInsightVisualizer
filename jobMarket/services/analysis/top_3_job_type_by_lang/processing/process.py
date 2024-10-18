from django.db.models import Count, F #, Window, FloatField, Q
# from django.db.models.functions import Rank
from jobMarket.models.shared import *
from jobMarket.models.all_models import *

### 전략
### 먼저 타겟으로 하는 포맷이 나오도록 집계를 해보고
### 쿼리 결과를 토대로 모델 생성후
### 인서트(create)

# 언어 스킬만 집계

def query_from_primaries(n_types=3):
    """Extracts data from tables tailored for the 4th chart
    Parameters:
    n_types (top n job subtypes to draw per language, default=3)
    """
    languages = (
        ### FROM
        JobSuperSubAssociation.objects
        ### WHERE
        .filter(
            # 새로운 공고 중에서만
            job_posting__is_new=True, 
            # 해당 링크가 속한 공고의 요구하는 스킬의 카테고리가 Languages이면
            job_posting__requirement__skill__skill_cat__name='Languages'
        )
        ### SELECT AS (var)
        .annotate(
            # F -> 이 전 호출된 구문 (여기서는 filter)의 결과 instance를 레퍼런스 하게 해줘유
            skill_name=F('job_posting__requirement__skill__name'),
            sub_type_name=F('sub_type__name'),
        )
        ### GROUP BY
        .values('skill_name', 'sub_type_name')
        ### SELECT COUNT AS (var)
        .annotate(subtype_count=Count('sub_type_name'))
    )
    ## => languages 인스턴스 안의 sub_type이름 컬럼은 최종적으로 sub_type_name이 됨

    # 언어별 잡 서브타입 카운트
    skill_totals = (
        languages
        .values('skill_name')
        .annotate(total_count=Count('sub_type_name'))
    )

    totals_dict = {entry['skill_name']: entry['total_count'] for entry in skill_totals}

    # 카운트 모아서 서브타입 백분율 환산
    percentages = [
        {
            'skill_name': entry['skill_name'],
            'sub_name': entry['sub_type_name'],
            'percentage': (entry['subtype_count'] * 100.0) / totals_dict[entry['skill_name']]
        }
        for entry in languages
    ]
    # percentages = (
    #     languages
    #     .annotate(
    #         total_count=F('skill_name__total_count'),
    #         percentage=(F('subtype_count') * 100.0 / F('total_count'))
    #     )
    # )

    # Rank-
    ranked = sorted(
        percentages,
        key=lambda x: (x['skill_name'], -x['percentage'])
    )
    # ranked = (
    #     percentages
    #     .annotate(
    #         rank=Window(
    #             expression=Rank(),
    #             partition_by=[F('skill_name')],
    #             order_by=F('percentage').desc()
    #         )
    #     )
    #     .filter(rank__lte=n_types)
    # )

    # Wrapping up
    result = {}
    for entry in ranked:
        skill_name = entry['skill_name']
        sub_type_name = entry['sub_name']
        percentage = entry['percentage']

        if skill_name not in result:
            result[skill_name] = {}

        if len(result[skill_name]) < n_types: # top 3 
            result[skill_name][sub_type_name] = f'{percentage:.2f}'

    # final = [
    #     {
    #         'lang': skill,
    #         'jobs': [
    #             {'job': subtype, 'percentage': percent}
    #             for subtype, percent in subtypes.items()
    #         ]
    #     } 
    #     for skill, subtypes in result.items()]

    final = [
        {skill:subtypes}
        for skill, subtypes in result.items()
    ]

    return final
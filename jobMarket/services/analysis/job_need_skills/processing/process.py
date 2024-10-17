from collections import defaultdict

from django.db.models import Count
from django.db import transaction

from jobMarket.models.all_models import *
from jobMarket.models.chart3model import *


@transaction.atomic
def chart3_secondary_tables():
    # 기존 데이터 삭제
    JobSkill.objects.all().delete()
    JobNeed.objects.all().delete()

    nested_dict = lambda: defaultdict(nested_dict)
    nest = nested_dict()
    
    experience_levels = [('신입', 'entry'), ('경력', 'experienced'), ('경력무관', 'all')]
    
    for job_sub_type in JobSubType.objects.all():

        # sub_type 중복 제거용.
        exists = JobNeed.objects.filter(job_name=job_sub_type.name)
        if not exists:
            job_need = JobNeed.objects.create(job_name=job_sub_type.name)
            nest[job_sub_type.name]["job_title"] = job_sub_type.name
        
        for experience_level, experience_name in experience_levels:
            skills = _get_skills_for_job_subtype(job_sub_type, experience_level)
            _update_skill_counts(nest, job_sub_type, experience_name, skills)

    
    for title, data in nest.items():
        job_need = JobNeed.objects.get(job_name=title)
        
        for exp_level in ["entry_tech_stacks", "experienced_tech_stacks"]:
            if exp_level in data:
                percentages = _calculate_percentages(data[exp_level])
                for skill_data in percentages:
                    JobSkill.objects.create(
                        job_need=job_need,
                        experience_level="신입" if exp_level == "entry_tech_stacks" else "경력",
                        skill=skill_data["tech_name"],
                        percentage=skill_data["percentage"]
                    )

def _get_skills_for_job_subtype(job_sub_type, experience_level):
    """
    job_sub_type과 experience_level로 필터링한 skills
    """
    return (
        Skill.objects
        .filter(
            requirement__job_posting__jobsupersubassociation__sub_type=job_sub_type,
            requirement__job_posting__experience_level=experience_level
        )
        .annotate(count=Count('id'))
        .order_by('-count')[:30]
    )

def _update_skill_counts(nest, job_sub_type, experience_name, skills):
    """
    skill 카운팅
    """
    for skill in skills:
        exp = nest[job_sub_type.name][f"{experience_name}_tech_stacks"]
        exp[skill.name] = exp[skill.name] + skill.count if exp[skill.name] else skill.count

def _calculate_percentages(data):
    """
    skill별 백분율 계산
    """
    total_count = sum(data.values())

    return [
        {
            "tech_name": skill,
            "percentage": round((count / total_count) * 100, 2)
        }
        for skill, count in data.items()
    ]
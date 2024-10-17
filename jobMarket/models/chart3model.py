from django.db import models
from .shared import BaseInfo


class JobNeed(BaseInfo):
    job_name = models.CharField(max_length=100, verbose_name="하위 직군 이름", unique=True)


class JobSkill(BaseInfo):
    job_need = models.ForeignKey(
        JobNeed, on_delete=models.PROTECT, verbose_name="기술 요구 직군"
    )
    experience_level = models.CharField(max_length=100, verbose_name="필요 경력 수준")
    skill = models.CharField(max_length=100, verbose_name="기술명")
    percentage = models.FloatField(verbose_name="백분율")
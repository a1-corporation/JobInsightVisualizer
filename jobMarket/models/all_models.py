from django.db import models
from .shared import BaseInfo

class Platform(BaseInfo):
    name = models.CharField(max_length=100, verbose_name="데이터 수집 플랫폼 이름")

class Company(BaseInfo):
    name = models.CharField(max_length=50, verbose_name='Company name')

class JobPosting(BaseInfo):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT)
    link = models.CharField(max_length=200, verbose_name='Job posting link')
    title = models.CharField(max_length=100, verbose_name='Posting title')
    experience_level = models.CharField(max_length=20, verbose_name='Job experience')
    is_new = models.BooleanField(default=True, verbose_name='Is this the revised one?')
    deadline = models.DateTimeField(verbose_name='Application deadline')
    collected_on = models.DateTimeField(verbose_name='Record scraped date', null=True)

class Location(BaseInfo):
    name = models.CharField(max_length=50, verbose_name='Workplace location')
    job_posting = models.ForeignKey(JobPosting, on_delete=models.PROTECT)

class SkillCategory(BaseInfo):
    name = models.CharField(max_length=100, verbose_name="기술 카테고리 이름")

class Skill(BaseInfo):
    skill_cat = models.ForeignKey(
        SkillCategory,
        on_delete=models.PROTECT,
        verbose_name="연관된 기술 카테고리 ID, skill_category 테이블과 참조됨",
    )
    name = models.CharField(max_length=100, verbose_name="기술의 이름")

class Requirement(BaseInfo):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)

class JobSuperType(BaseInfo):
    name = models.CharField(max_length=100, verbose_name="상위 직군 이름")

class JobSubType(BaseInfo):
    super_type = models.ForeignKey(
        JobSuperType, on_delete=models.PROTECT, verbose_name="상위 직군의 ID"
    )
    name = models.CharField(max_length=100, verbose_name="하위 직군 이름")

class JobSuperSubAssociation(BaseInfo):
    job_posting = models.ForeignKey(
        JobPosting, on_delete=models.PROTECT, verbose_name="채용 공고 ID"
    )
    super_type = models.ForeignKey(
        JobSuperType, on_delete=models.PROTECT, verbose_name="상위 직군의 ID"
    )
    sub_type = models.ForeignKey(
        JobSubType, on_delete=models.PROTECT, verbose_name="하위 직군의 ID"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["job_posting", "sub_type"],
                name="unique_job_super_sub_association",
            )
        ]
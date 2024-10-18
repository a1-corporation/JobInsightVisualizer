from django.db import models
from django.core.validators import MinValueValidator
from .shared import BaseInfo


class PostingByJobPosition(BaseInfo):
    collected_on = models.DateTimeField(verbose_name="데이터 수집 일시")
    job_sub_type_name = models.CharField(max_length=100, verbose_name="하위 직군 이름")
    count = models.IntegerField(
        verbose_name="공고 수", validators=[MinValueValidator(0)]
    )

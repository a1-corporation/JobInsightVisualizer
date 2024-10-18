from django.db import models

from .shared import BaseInfo


class PostingByJobLocation(BaseInfo):
   location_name = models.CharField(max_length=50, verbose_name='지역 이름')
   experience_level = models.CharField(max_length=20, verbose_name='경력')
   rate = models.FloatField(verbose_name='백분율')
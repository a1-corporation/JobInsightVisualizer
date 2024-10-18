from django.db import models
from jobMarket.models.shared import *

class ChartFour(BaseInfo):
    language = models.CharField(max_length=50, verbose_name="언어")
    role = models.CharField(max_length=50, verbose_name="직무")
    percentage = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="비율")

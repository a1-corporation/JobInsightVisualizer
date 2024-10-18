from django.db import models
from .shared import BaseInfo

class RawFile(BaseInfo):
    filename = models.CharField(max_length=100, verbose_name='File name')
    collected_on = models.DateTimeField(verbose_name='Record scraped date', null=True)
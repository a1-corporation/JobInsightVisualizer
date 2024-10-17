from django.urls import path
from .services.analysis.top_3_job_type_by_lang.delivery import chart4view
from .services.analysis.job_need_skills.delivery import chart3view

app_name = 'jobMarket'
urlpatterns = [
    path('top_3_job_type_by_lang/', chart4view.chartfour, name='chart4'),
    path('job_need_skills/', chart3view.chartthree, name='chart3'),
]
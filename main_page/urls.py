from django.urls import path
from . import views

urlpatterns = [
    path('show_chart/', views.main_page, name='show_chart'),
    path('', views.index, name='index'),
    path('index_test/', views.index_test, name='index_test'),
    path('job_postings_count_chart/', views.job_postings_count_chart, name='job_postings_count_chart'),
    path('job_postings_count_by_experience_chart/', views.job_postings_count_by_experience_chart, name='job_postings_count_by_experience_chart'),
    path('entry_tech_stacks_chart/', views.entry_tech_stacks_chart, name='entry_tech_stacks_chart'),
    path('experienced_tech_stacks_chart/', views.experienced_tech_stacks_chart, name='experienced_tech_stacks_chart'),
    # path('layered_donut_chart/', views.layered_donut_chart, name='layered_donut_chart'),
    # path('word_cloud/', views.word_cloud, name='word_cloud'),
    path('word_cloud_new/', views.word_cloud_new, name='word_cloud_new'),
    path('word_cloud_experienced/', views.word_cloud_experienced, name='word_cloud_experienced'),

    path('show_chart/', views.main_page, name='show_chart'),

]

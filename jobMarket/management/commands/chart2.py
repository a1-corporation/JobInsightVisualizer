from django.core.management.base import BaseCommand
from jobMarket.services.analysis.posting_by_job_location.processing.process import chart2_secondary_tables


class Command(BaseCommand):
    help = 'job_need_skills 관련 데이터 추출/변환/적재 작업을 수행'
    
    def handle(self, *args, **options):
        chart2_secondary_tables()
        
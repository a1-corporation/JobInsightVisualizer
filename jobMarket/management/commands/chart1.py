from django.core.management.base import BaseCommand

from jobMarket.services.analysis.posting_by_job_position.processing import Pipeline


class Command(BaseCommand):
    help = "posting_by_job_position 관련 데이터 추출/변환/적재 작업을 수행한다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--start_date", type=str, help="시작 날짜를 입력하세요. (YYYY-MM-DD)."
        )
        parser.add_argument(
            "--end_date", type=str, help="종료 날짜를 입력하세요. (YYYY-MM-DD)."
        )

    def handle(self, *args, **options) -> None:
        Pipeline.run(options)

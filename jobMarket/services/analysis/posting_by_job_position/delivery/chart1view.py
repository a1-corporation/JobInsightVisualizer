from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from jobMarket.models import PostingByJobPosition
from jobMarket.serializers import *

from datetime import timedelta
from django.utils.dateparse import parse_date
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class PostingByJobPositionView(APIView):

    @swagger_auto_schema(
        operation_summary="조회일 기준 최근 7일간 특정 직무의 일별 공고 수를 제공하는 API",
        operation_description="특정 직무에 대한 일별 공고 수를 날짜별로 제공하는 데이터 API입니다. 기준일을 포함한 최근 7일 간의 데이터를 제공합니다.",
        query_serializer=PostingByJobPositionQuerySerializer,
        responses={
            200: openapi.Response(
                description="OK - 요청한 조건에 맞는 데이터를 반환합니다.",
                schema=PostingByJobPositionSerializer(many=True),
            ),
            400: openapi.Response(
                description="Bad Request - 필수 파라미터를 보내지 않았거나, 파라미터 양식이 잘못되었을 때 돌아오는 응답입니다.",
                examples={
                    "application/json": {
                        "datetime": ["날짜는 YYYY-MM-DD 양식으로 입력해주세요."]
                    }
                },
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        query_serializer = PostingByJobPositionQuerySerializer(data=request.GET)

        if not query_serializer.is_valid():
            return Response(query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        end_date_str = query_serializer.validated_data["datetime"]
        job_type = query_serializer.validated_data["job_type"]

        end_date = parse_date(end_date_str)
        start_date = end_date - timedelta(days=6)

        data = PostingByJobPosition.objects.filter(
            collected_on__gte=start_date,
            collected_on__lte=end_date,
            job_sub_type_name=job_type,
        )

        serializer = PostingByJobPositionSerializer(data, many=True)

        return Response(serializer.data)

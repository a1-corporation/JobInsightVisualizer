from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from jobMarket.models.shared import *
from jobMarket.models.chart3model import *
from jobMarket.models.chart2model import *
from .chart2serializers import *


class PostingByJobLocationView(APIView):

    @swagger_auto_schema(
        operation_summary="각 지역별 공고의 요구 경력 비율을 제공하는 API",
        operation_description="각 지역별 공고에서 요구하는 경력 비율을 제공하는 데이터 API입니다. 각 지역을 기준으로 신입, 경력, 경력무관의 비율이 제공됩니다.",
        responses={
            200: openapi.Response(
                description="OK - 요청한 조건에 맞는 데이터를 반환합니다.",
                schema=PostingByJobLocationSerializer(many=True),
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        """Non-browsible API for chart 2
        Parameters:
        request
        """
        result = PostingByJobLocation.objects.all()
        serializer = PostingByJobLocationSerializer(result, many=True)

        return Response(serializer.data)

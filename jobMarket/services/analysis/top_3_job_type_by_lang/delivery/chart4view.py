from jobMarket.models.shared import *
from jobMarket.models.chart4model import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

subtype_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "job": openapi.Schema(type=openapi.TYPE_STRING, description='Role'),
        "percentage": openapi.Schema(type=openapi.TYPE_STRING, description="Ratio")
    }
)
languange_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'lang': openapi.Schema(type=openapi.TYPE_STRING, description="programming language"),
        "jobs": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=subtype_schema,
            description="List of roles with percentages"
        )
    }
)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve chart data for languages and job roles.",
    responses={
        200: openapi.Response(
        description="A list of languages and their associated job roles.",
        schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=languange_schema
        )
    )}
)

@api_view(['GET'])
def chartfour(request):
    """Non-browsible API for chart 4"""
    records = ChartFour.objects.all()

    reorganized = {}
    for record in records:
        language = record.language,
        role = record.role,
        percentage = f'{record.percentage:.2f}%'
        
        if language not in reorganized:
            reorganized[language] = {}
        
        reorganized[language][role] = percentage

    # 왜 리스트로 반환대지
    result = [
        {
            "lang": lang[0],
            "jobs": [
                { "job": role[0], "percentage": percentage }
                for role, percentage in roles.items()
            ]
        }
        for lang, roles in reorganized.items()
    ]

    return Response(result)
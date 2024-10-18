from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.decorators import api_view

from jobMarket.models.shared import *
from jobMarket.models.chart3model import *

tech_stack_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "tech_name": openapi.Schema(type=openapi.TYPE_STRING, description="Skill"),
        "percentage": openapi.Schema(type=openapi.TYPE_NUMBER, description="Ratio")
    }
)

job_need_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "job_title": openapi.Schema(type=openapi.TYPE_STRING, description="Job name"),
        "entry_tech_stacks": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=tech_stack_schema,
            description="Entry level need skills"
        ),
        "experienced_tech_stacks": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=tech_stack_schema,
            description="Experienced level need skills"
        )
    }
)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve chart data for skill and job experience level.",
    responses={
        200: openapi.Response(
            description="A list of skill and their associated job experience level.",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=job_need_schema
            )
        )
    }
)

@api_view(['GET'])
def chartthree(request):
    """Non-browsible API for chart 3
    Parameters:
    request
    """
    result = []
    for job_need in JobNeed.objects.all():
        tech_stack = {
            "job_title": job_need.job_name,
            "entry_tech_stacks": [],
            "experienced_tech_stacks": []
        }
        
        entry_skills = job_need.jobskill_set.filter(experience_level="신입").order_by('-percentage')
        experienced_skills = job_need.jobskill_set.filter(experience_level="경력").order_by('-percentage')
        
        tech_stack["entry_tech_stacks"] = [
            {"tech_name": skill.skill, "percentage": float(skill.percentage)}
            for skill in entry_skills
        ]

        
        tech_stack["experienced_tech_stacks"] = [
            {"tech_name": skill.skill, "percentage": float(skill.percentage)}
            for skill in experienced_skills
        ]
        tech_stack["entry_tech_stacks"].sort(key=lambda x: x["percentage"], reverse=True)
        tech_stack["experienced_tech_stacks"].sort(key=lambda x: x["percentage"], reverse=True)
        
        result.append(tech_stack)

    return Response(result)
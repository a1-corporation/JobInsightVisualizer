from rest_framework import serializers
from datetime import datetime
from .models import *

from .constants import JOB_SUB_TYPE_NAMES


class PostingByJobPositionQuerySerializer(serializers.Serializer):
    datetime = serializers.CharField(
        default=datetime.today().strftime("%Y-%m-%d"),
        min_length=10,
        max_length=10,
        help_text="데이터 조회 기준 일자 (YYYY-MM-DD)",
    )
    job_type = serializers.ChoiceField(
        choices=JOB_SUB_TYPE_NAMES, required=True, help_text="하위 직군 이름"
    )

    def validate_datetime(self, value) -> str:
        if len(value) != 10:
            raise serializers.ValidationError(
                "날짜는 YYYY-MM-DD 형식으로 입력해야 합니다."
            )

        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise serializers.ValidationError(
                "날짜는 YYYY-MM-DD 형식으로 입력해야 합니다."
            )

        return value

    def validate_job_type(self, value: str) -> str:
        if value not in JOB_SUB_TYPE_NAMES:
            raise serializers.ValidationError("정확한 세부 직무명을 입력해주세요.")

        return value


class PostingByJobPositionSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(
        source="collected_on",
        label=PostingByJobPosition._meta.get_field("collected_on").verbose_name,
    )
    job_type = serializers.CharField(
        source="job_sub_type_name",
        label=PostingByJobPosition._meta.get_field("job_sub_type_name").verbose_name,
    )

    class Meta:
        model = PostingByJobPosition
        fields = ["datetime", "job_type", "count"]

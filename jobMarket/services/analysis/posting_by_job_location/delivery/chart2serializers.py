from rest_framework import serializers
from jobMarket.models import PostingByJobLocation


class PostingByJobLocationSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(
        label=PostingByJobLocation._meta.get_field("location_name").verbose_name,
    )

    experience_level = serializers.CharField(
        label=PostingByJobLocation._meta.get_field("experience_level").verbose_name,
    )

    rate = serializers.FloatField(
        label=PostingByJobLocation._meta.get_field("rate").verbose_name,
    )

    class Meta:
        model = PostingByJobLocation
        fields = ["location_name", "experience_level", "rate"]

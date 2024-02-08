# healthRecords/serializers.py

from rest_framework import serializers
from .models import HealthRecord
from drf_extra_fields.fields import Base64ImageField


class HealthRecordSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = HealthRecord
        fields = '__all__'

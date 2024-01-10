# healthRecords/serializers.py

from rest_framework import serializers
from .models import HealthRecord


class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['id', 'user', 'name', 'abhaNumber',
                  'aadharNumber', 'centerName']

# healthRecords/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import HealthRecord
from .serializers import HealthRecordSerializer


class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

    @action(detail=False, methods=['GET'])
    def get_records_for_user(self, request):
        user_id = request.query_params.get('user_id')

        # Validate if user_id is provided in the request
        if not user_id:
            return Response({'error': 'Please provide user_id parameter in the request.'}, status=400)

        # Filter health records based on user_id
        health_records = HealthRecord.objects.filter(user__id=user_id)

        # Serialize the data
        serializer = HealthRecordSerializer(health_records, many=True)

        return Response(serializer.data)

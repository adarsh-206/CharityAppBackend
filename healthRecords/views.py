# healthRecords/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import HealthRecord
from .serializers import HealthRecordSerializer
from rest_framework import status
from authentication.models import User
from django.utils import timezone


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

    @action(detail=False, methods=['POST'])
    def create_records_for_user(self, request):
        user_id = request.query_params.get('user_id')

        # Validate if user_id is provided in the request
        if not user_id:
            return Response({'error': 'Please provide user_id parameter in the request.'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract data from the request
        records_data = request.data
        user = User.objects.get(id=user_id)

        # Iterate through each record and create HealthRecord objects
        for record_data in records_data:
            record_data['user'] = user.id  # Assign the user to the record
            serializer = HealthRecordSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Health records created successfully.'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def get_records_counts(self, request):
        user_id = request.query_params.get('user_id')

        # Validate if user_id is provided in the request
        if not user_id:
            return Response({'error': 'Please provide user_id parameter in the request.'}, status=400)

        # Get total health records count for the user
        total_records_count = HealthRecord.objects.filter(
            user__id=user_id).count()

        # Get health records count registered on today's date
        today = timezone.now().date()
        today_records_count = HealthRecord.objects.filter(
            user__id=user_id, created_at__date=today).count()

        return Response({
            'user_id': user_id,
            'total_records_count': total_records_count,
            'today_records_count': today_records_count
        })

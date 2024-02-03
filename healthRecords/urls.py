# healthRecords/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthRecordViewSet

router = DefaultRouter()
router.register(r'health-records', HealthRecordViewSet,
                basename='health-record')

urlpatterns = [
    path('', include(router.urls)),
    path('create-records/', HealthRecordViewSet.as_view(
        {'post': 'create_records_for_user'}), name='create-records'),
]

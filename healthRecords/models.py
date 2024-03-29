from django.db import models
from authentication.models import User
from django.utils import timezone


class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    abhaNumber = models.CharField(max_length=255)
    aadharNumber = models.CharField(max_length=255)
    centerName = models.CharField(max_length=255)
    birthYear = models.CharField(max_length=15, blank=True, null=True)
    mobileNumber = models.CharField(max_length=10, blank=True, null=True)
    fatherHusbandName = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    maritalStatus = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    caste = models.CharField(max_length=50, blank=True, null=True)
    subCaste = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pinCode = models.CharField(max_length=10, blank=True, null=True)
    medication = models.CharField(max_length=3, blank=True, null=True)
    bloodTransfusion = models.CharField(max_length=3, blank=True, null=True)
    familyHistory = models.CharField(max_length=3, blank=True, null=True)
    image = models.CharField(blank=True, null=True, max_length=1000000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.loginID} - {self.name}"

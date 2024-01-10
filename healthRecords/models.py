from django.db import models
from authentication.models import User


class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    abhaNumber = models.CharField(max_length=255)
    aadharNumber = models.CharField(max_length=255)
    centerName = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.loginID} - {self.name}"

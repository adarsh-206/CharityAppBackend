# authentication/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, loginID, name, password=None, mobile_number=None, aadhar_number=None, **extra_fields):
        if not loginID:
            raise ValueError('The Login ID must be set')
        user = self.model(loginID=loginID, name=name, mobile_number=mobile_number,
                          aadhar_number=aadhar_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, loginID, name, password=None, mobile_number=None, aadhar_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(loginID, name, password, mobile_number=mobile_number, aadhar_number=aadhar_number, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    loginID = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    aadhar_number = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'loginID'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.loginID

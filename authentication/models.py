# authentication/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, loginID, name, password=None, **extra_fields):
        if not loginID:
            raise ValueError('The Login ID must be set')
        user = self.model(loginID=loginID, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, loginID, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(loginID, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    loginID = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Additional fields
    abhaNumber = models.CharField(max_length=255, blank=True)
    aadharNumber = models.CharField(max_length=255, blank=True)
    centerName = models.CharField(max_length=255, blank=True)
    birthYear = models.CharField(max_length=4, blank=True)
    mobileNumber = models.CharField(max_length=10, blank=True)
    fatherHusbandName = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    maritalStatus = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=50, blank=True)
    caste = models.CharField(max_length=50, blank=True)
    subCaste = models.CharField(max_length=50, blank=True)
    house = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    pinCode = models.CharField(max_length=10, blank=True)
    medication = models.CharField(max_length=3, blank=True)
    bloodTransfusion = models.CharField(max_length=3, blank=True)
    familyHistory = models.CharField(max_length=3, blank=True)
    image = models.CharField(max_length=255, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'loginID'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.loginID

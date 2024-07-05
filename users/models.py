from django.db import models
from core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_ROLES = (
    ("Admin", "Admin"),
    ("Collector", "Collector"),
    ("Employee", "Employee"),
)
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=USER_ROLES)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
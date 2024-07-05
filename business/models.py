from django.db import models
from core.models import AbstractBaseModel
# Create your models here.
class Business(AbstractBaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True)
    postal_address = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Apartment(AbstractBaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255)
    tenants_registered = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Tenant(AbstractBaseModel):
    appartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    id_number = models.CharField(max_length=255, null=True)
    house_number = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
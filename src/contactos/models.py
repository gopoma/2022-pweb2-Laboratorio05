from django.db import models

# Create your models here.
class Contacto(models.Model):
    isFamiliar = models.BooleanField(default=False)
    fullname = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
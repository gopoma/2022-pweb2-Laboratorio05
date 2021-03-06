from django.db import models
from django.urls import reverse

# Create your models here.
class Estudiante(models.Model):
    cui = models.CharField(max_length=8)
    fullname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=9)
    graduated = models.BooleanField(default=False)
    state = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    district = models.CharField(blank=True, max_length=255) 

    def get_absolute_url(self):
        return reverse("estudiantes:estudiante-detail", kwargs={"pk": self.id})
    def __str__(self):
        return self.fullname
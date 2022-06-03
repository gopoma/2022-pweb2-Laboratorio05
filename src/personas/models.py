from django.db import models

# Create your models here.
class Persona(models.Model):
    names = models.TextField()
    surnames = models.TextField()
    age = models.TextField()

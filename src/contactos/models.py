from django.db import models

# Create your models here.
class Contacto(models.Model):
    isFamiliar = models.BooleanField(default=False)
    fullname = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    state = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.fullname} ({'Yes' if self.isFamiliar else 'No'})"
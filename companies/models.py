from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " - " + str(self.company.nombre)
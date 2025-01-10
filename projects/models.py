from django.db import models
from companies.models import Company

# Create your models here.
class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return str(self.company.nombre) + " - " + str(self.nombre)



class UserStory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return str(self.project.nombre) + " - " + str(self.nombre)


class Ticket(models.Model):
    userStory = models.ForeignKey(UserStory, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    
    class Estado(models.IntegerChoices):
        activo = 1, "Activo"
        enProceso = 2, "En proceso"
        finalizado = 3, "Finalizado"
        # (...)

    estado = models.PositiveSmallIntegerField(
        choices=Estado.choices,
        default=Estado.activo
    )


    def __str__(self):
        return str(self.userStory.nombre) + " - " + str(self.nombre)
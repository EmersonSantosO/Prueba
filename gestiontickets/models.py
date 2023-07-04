from django.db import models
import uuid
from django.urls import reverse

class Especialidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class SoporteTI(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    especialidades = models.ManyToManyField(Especialidad)
    imagen_perfil = models.ImageField(upload_to='perfil/')

    def __str__(self):
        return self.nombre


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    soporte = models.ForeignKey(SoporteTI, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('ticket-detail', args=[str(self.id)])
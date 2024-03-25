from django.db import models
from django.contrib.auth.models import User

class Solicitudes(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_finalización = models.DateTimeField(null=True, blank=True)
    urgente = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' by ' + self.usuario.username

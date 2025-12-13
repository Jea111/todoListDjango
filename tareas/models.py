from django.db import models
from usuarios.models import Usuarios
# Create your models here.from django.db import models
from usuarios.models import Usuarios

class Tareas(models.Model):
    nombre_tarea = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_finalizada = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return f'{self.nombre_tarea} por {self.usuario.nombre_usuario}'

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-fecha_creada']  
    
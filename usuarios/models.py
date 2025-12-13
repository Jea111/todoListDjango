from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='perfiles/',blank=True,null=True)
    residencia = models.CharField(max_length=100)
    correo = models.EmailField()
    password = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nombre_usuario} '
    
    class Meta:
       
        verbose_name = 'Usario'
        verbose_name_plural = 'Usuarios'
    
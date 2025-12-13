from django.contrib import admin
from .models import Tareas

class TareasItem(admin.ModelAdmin):
    fields = ['nombre_tarea', 'descripcion', 'usuario', 'estado', 'fecha_finalizada']
    list_display = ['nombre_tarea', 'usuario', 'estado', 'fecha_creada', 'fecha_finalizada']
    list_filter = ['usuario', 'estado']
    search_fields = ['nombre_tarea', 'descripcion', 'usuario__nombre_usuario']

admin.site.register(Tareas, TareasItem)

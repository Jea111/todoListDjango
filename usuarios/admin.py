from django.contrib import admin
from . models import Usuarios
# Register your models here.

class usuariosItem(admin.ModelAdmin):
    fields = ['nombre_usuario','foto_perfil','residencia','correo','password']
    list_display = ['nombre_usuario','residencia','correo','create_at']
    list_filter = ['nombre_usuario','correo','create_at']
    search_fields = ['nombre_usuario','residencia','correo','create_at']
    
admin.site.register(Usuarios,usuariosItem)

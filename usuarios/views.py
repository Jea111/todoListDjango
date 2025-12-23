from django.shortcuts import render, redirect
from .models import Usuarios
from tareas.models import Tareas

def crear_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        foto_perfil = request.FILES.get('foto_perfil')
        residencia = request.POST.get('residencia')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        #Obtener o crear usuario
        usuario, creado = Usuarios.objects.get_or_create(
            nombre_usuario=nombre_usuario,
            defaults={
                'foto_perfil': foto_perfil,
                'residencia': residencia,
                'correo': correo,
                'password': password
            }
        )

        # datos de la tarea     
        nombre_tarea = request.POST.get('nombre_tarea')
        descripcion = request.POST.get('descripcion')
        fecha_finalizada = request.POST.get('fecha_finalizada')

        # crear tarea relacionado al usuario
        Tareas.objects.create(
            nombre_tarea=nombre_tarea,
            descripcion=descripcion,
            usuario=usuario,
            fecha_finalizada=fecha_finalizada
        )

        return redirect('tareas')

    return render(request, 'crear_tareas.html')

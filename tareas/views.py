from django.shortcuts import render,redirect
from django.shortcuts import render, redirect, get_object_or_404

from . models import Tareas
from usuarios.models import Usuarios
# # Create your views here.
        
        
def tareasAllViews(request):
    tareas = Tareas.objects.all().order_by('fecha_creada')
    return render(request,'vista_tareas.html',{'tareas':tareas})





def editar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)

    if request.method == 'POST':
        tarea.nombre_tarea = request.POST.get('nombre_tarea')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.fecha_finalizada = request.POST.get('fecha_finalizada')
        tarea.estado = bool(request.POST.get('estado'))

        tarea.save()  
        return redirect('tareas')

    return render(request, 'editar_tarea.html', {'tarea': tarea})


def eliminar_tarea(request,id):
    tarea = get_object_or_404(Tareas, id=id)
    usuario = tarea.usuario  

    tarea.delete()

    if not Tareas.objects.filter(usuario=usuario).exists():
        usuario.delete()

    return redirect('tareas')
    
def editar_usuario(request,id):
    usuario = get_object_or_404(Usuarios,id=id)
    if request.method =='POST':
        usuario.nombre_usuario = request.POST.get('nombre_usuario')
        if request.FILES.get('foto_perfil'):
            
            usuario.foto_perfil = request.FILES.get('foto_perfil')
        
        usuario.residencia = request.POST.get('residencia')
        usuario.correo = request.POST.get('correo')
        usuario.password = request.POST.get('password')
        usuario.save()
        return redirect('tareas')
    return render(request,'editar_usuario.html',{'usuario':usuario})
  
  

def buscador_tareas_por_nombre(request):
    """Busqueda de tareas por nombre de usuario"""
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        tareas_filtradas = Tareas.objects.filter(
    usuario__nombre_usuario__icontains=busqueda
)

        return render(request,'busqueda_tareas_usuario.html',{'busqueda':busqueda,'tareas_filtradas':tareas_filtradas})
    return redirect('tareas')


def validar_usuario(request):
    "Login para admin"
    if request.method == 'POST':
        username = request.POST.get('b')
        password = request.POST.get('p')
        usuario = Usuarios.objects.filter(nombre_usuario=username,password=password).first()
        if usuario:
            return redirect('tareas')
            
        else:
            mensaje = 'Debes ser un usuario registrado para agg tareas'
            return render(request,'validar_usuario.html',{'mensaje':mensaje})
            
            
    return render(request,'validar_usuario.html')
    
        
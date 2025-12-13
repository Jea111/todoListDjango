from django.shortcuts import render
from . models import Tareas
from usuarios.models import Usuarios
# Create your views here.
def createTarea(request):
    # crear usuario
    if request.method =='POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        foto_perfil = request.FILES.get('foto_perfil')
        residencia = request.POST.get('residencia')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        
        usuario = Usuarios.objects.create(nombre_usuario=nombre_usuario,foto_perfil=foto_perfil,residencia=residencia,correo=correo,password=password)
        
        # crear tarea 
        
    if request.method == 'POST':
        nombre_tarea= request.POST.get('nombre_tarea')
        descripcion= request.POST.get('descripcion')
        fecha_finalizada= request.POST.get('fecha_finalizada')
        
        Tareas.objects.create(nombre_tarea=nombre_tarea,descripcion=descripcion,usuario=usuario,fecha_finalizada=fecha_finalizada)
        return render(request,'crear_tareas.html')
    return render(request,'crear_tareas.html')
            
        
        
def tareasAllViews(request):
    tareas = Tareas.objects.all().order_by('fecha_creada')
    return render(request,'vista_tareas.html',{'tareas':tareas})

    

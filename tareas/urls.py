from django.urls import path
from .views import createTarea,tareasAllViews,editar_tarea,eliminar_tarea,editar_usuario

urlpatterns = [
    path('crearTarea',createTarea,name='crearTarea'),
    path('',tareasAllViews,name='tareas'),
    path('editar_tarea/<int:id>/',editar_tarea,name='editar_tarea'),
    path('eliminar_tarea/<int:id>/',eliminar_tarea,name='eliminar_tarea'),
    path('editar_usuario/<int:id>/',editar_usuario,name='editar_usuario'),
]

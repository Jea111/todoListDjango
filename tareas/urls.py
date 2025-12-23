from django.urls import path
from .views import createTarea,tareasAllViews,editar_tarea,eliminar_tarea,editar_usuario,buscador_tareas_por_nombre,validar_usuario

urlpatterns = [
    path('crearTarea',createTarea,name='crearTarea'),
    path('tareas',tareasAllViews,name='tareas'),
    path('editar_tarea/<int:id>/',editar_tarea,name='editar_tarea'),
    path('eliminar_tarea/<int:id>/',eliminar_tarea,name='eliminar_tarea'),
    path('editar_usuario/<int:id>/',editar_usuario,name='editar_usuario'),
    path('tareas_filtradas',buscador_tareas_por_nombre,name='tareas_filtradas'),
    path('',validar_usuario,name='validar_usuario'),

]

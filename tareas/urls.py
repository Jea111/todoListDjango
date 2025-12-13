from django.urls import path
from .views import createTarea,tareasAllViews

urlpatterns = [
    path('',createTarea,name='crearTarea'),
    path('tareas/',tareasAllViews,name='tareas')
]

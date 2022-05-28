from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  #Esta era nuestra primera view
    path('cursos', views.cursos, name="Cursos"),
    path('entregables', views.entregables, name="Entregables"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesores', views.profesores, name="Profesores"),
]
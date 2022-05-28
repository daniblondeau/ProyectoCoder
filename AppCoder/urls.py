from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  #Esta era nuestra primera view
    path('cursos', views.cursos, name="Cursos"),
    path('entregables', views.entregables, name="Entregables"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesores', views.profesores, name="Profesores"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
]
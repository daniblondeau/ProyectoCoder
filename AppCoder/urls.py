from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.index, name="index"),  #Esta era nuestra primera view
    path('agregar_curso/', views.agregar_curso, name="agregar_curso"),
    path('agregar_profesor/', views.agregar_profesor, name="agregar_profesor"),
    path('agregar_estudiante/', views.agregar_estudiante, name="agregar_estudiante"),
    path('buscar_curso/', views.buscar_curso, name="buscar_curso"),
    path('buscar_profesor/', views.buscar_profesor, name="buscar_profesor"),
    path('buscar_estudiante/', views.buscar_estudiante, name="buscar_estudiante"),
]
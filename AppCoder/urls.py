from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),  #Esta era nuestra primera view
    path('cursos', views.cursos, name="Cursos"),
    path('entregables', views.entregables),
    path('estudiantes', views.estudiantes),
    path('profesores', views.profesores),
]
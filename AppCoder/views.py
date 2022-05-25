from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada:{curso.camada}"

    return HttpResponse(documentoDeTexto)

def inicio(request):
    #return HttpResponse('vista inicio')
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    #return HttpResponse('vista cursos')
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    #return HttpResponse('vista profesores')
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    #return HttpResponse('vista estudiantes')
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    #return HttpResponse('vista entregables')
    return render(request, "AppCoder/entregables.html")
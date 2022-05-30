from curses.ascii import HT
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from AppCoder.forms import BuscarCursoForm, BuscarEstudianteForm, BuscarProfesorForm, CursoForm, ProfesorForm, EstudianteForm
from AppCoder.models import Curso, Estudiante, Profesor

def index(request):
    return render(request, "AppCoder/index.html")

def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            camada = form.cleaned_data['camada']
            Curso(curso=curso, camada=camada).save()
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = CursoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'AppCoder/form_carga_curso.html', {'form': form})


def agregar_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesion = form.cleaned_data['profesion']
            Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion).save()
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = ProfesorForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'AppCoder/form_carga_profesor.html', {'form': form})


def agregar_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            Estudiante(nombre=nombre, apellido=apellido, email=email).save()
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = EstudianteForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'AppCoder/form_carga_estudiante.html', {'form': form})


def buscar_curso(request):
    if request.method == "GET":
        form_busqueda_curso = BuscarCursoForm()
        return render(request, 'AppCoder/form_busqueda_curso.html', {"form_busqueda_curso": form_busqueda_curso})
    elif request.method == "POST":
        form_busqueda_curso = BuscarCursoForm(request.POST)
        if form_busqueda_curso.is_valid():
            palabra_a_buscar = form_busqueda_curso.cleaned_data['palabra_a_buscar']
            cursos = Curso.objects.filter(camada__icontains=palabra_a_buscar)
    return  render(request, 'AppCoder/lista_cursos.html', {"cursos": cursos})

def buscar_estudiante(request):
    if request.method == "GET":
        form_busqueda_estudiante = BuscarEstudianteForm()
        return render(request, 'AppCoder/form_busqueda_estudiante.html', {"form_busqueda_estudiante": form_busqueda_estudiante})
    elif request.method == "POST":
        form_busqueda_estudiante = BuscarEstudianteForm(request.POST)
        if form_busqueda_estudiante.is_valid():
            palabra_a_buscar = form_busqueda_estudiante.cleaned_data['palabra_a_buscar']
            estudiantes = Estudiante.objects.filter(nombre__icontains=palabra_a_buscar)
    return  render(request, 'AppCoder/lista_estudiantes.html', {"estudiantes": estudiantes})

def buscar_profesor(request):
    if request.method == "GET":
        form_busqueda_profesor = BuscarProfesorForm()
        return render(request, 'AppCoder/form_busqueda_profesor.html', {"form_busqueda_profesor": form_busqueda_profesor})
    elif request.method == "POST":
        form_busqueda_profesor = BuscarProfesorForm(request.POST)
        if form_busqueda_profesor.is_valid():
            palabra_a_buscar = form_busqueda_profesor.cleaned_data['palabra_a_buscar']
            profesores = Profesor.objects.filter(nombre__icontains=palabra_a_buscar)
    return  render(request, 'AppCoder/lista_profesores.html', {"profesores": profesores})
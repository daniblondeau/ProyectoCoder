from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario, ProfesorFormulario
#def curso(self):
#    curso = Curso(nombre="Desarrollo Web", camada="19881")
#    curso.save()
#    documentoDeTexto = f"--->Curso: {curso.nombre} Camada:{curso.camada}"
#
#    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST) #Aqui llega toda la informacion del html.
        print(miFormulario)
        
        if miFormulario.is_valid:  #Si pasó la validación de Django.
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")  #Vuelvo al inicio o donde se desee.
    
    else:
        miFormulario = CursoFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST) #Aqui llega toda la informacion del html.
        print(miFormulario)
        
        if miFormulario.is_valid:  #Si pasó la validación de Django.
            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'],)
            profesor.save()
            return render(request, "AppCoder/inicio.html")  #Vuelvo al inicio o donde se desee.
    
    else:
        miFormulario = ProfesorFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
     return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    return HttpResponse(respuesta)
#    if request.GET["camada"]:
#        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
#        camada = request.GET['camada']
#        cursos = Curso.objects.filter(camada__icontains = camada)
#        
#        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
#    else:
#        respuesta = "No enviaste datos"
#    #No olvidar from django.http impost HttpResponse
#    return HttpResponse(respuesta)
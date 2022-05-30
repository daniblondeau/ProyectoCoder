import email
from django import forms

class CursoForm(forms.Form):
    #Especificar los campos
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class ProfesorForm(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteForm(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class BuscarEstudianteForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarProfesorForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarCursoForm(forms.Form):
    palabra_a_buscar = forms.IntegerField(label="Buscar")
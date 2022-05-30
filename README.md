# Proyecto AppCoder

En la aplicacion **AppCoder** se pueden *Agregar* y *Buscar*:

* Cursos
* Estudiantes
* Profesores


## Requerimientos:

* Tener instalado:
  * Python
  * Django
  * Django bootstrap v5

<br>

***

## Como probar la app?

1. Descargar o Clonar el repositorio.
2. Sobre el directorio raiz (donde se encuentra el archivo *manage.py*) correr el comando:
   ```
   python manage.py runserver
   ```
3. Ingresar al: [localhost](http://localhost:8000/)

<br>

### Como agregar valores a la base de datos?

1. Click sobre alguna de las opciones: Agregar Curso, Agregar Profesor o Agregar Estudiantes.
2. Completar el formulario.
3. Click sobre el boton **Guardar**.

### Como buscar un valor en la base de datos?

1. Click sobre alguna de las opciones: Buscar Curso, Buscar Profesor o Buscar Estudiantes.
2. Ingresar el valor buscado.
3. Click sobre el boton **Buscar**.

> Para tener en cuenta, dados los tipos de valores para el caso de Estudiantes y Profesores se buscaran caracteres, y para el caso de Cursos valores numericos.
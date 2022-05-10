from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Avatar
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import User

# from ProyectoCoder.AppCoder.models import Avatar
# Create your views here.



# @login_required
def inicio(request):
      if request.user.is_authenticated:
            avatares = Avatar.objects.filter(user=request.user.id)

            return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})
      else:
            return render(request,"AppCoder/inicio.html")


def about(request):
      return render(request,"AppCoder/about.html")







def cursos(request):

      cursos = Curso.objects.all() #trae todos los profesores

      contexto= {"cursos":cursos} 
      avatares = Avatar.objects.filter(user=request.user.id)

      return render(request, "AppCoder/Cursos.html",contexto)


@login_required
def agregarCurso(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['nombre'], camada=informacion['camada'])

                  curso.save()

                  return render(request, "AppCoder/Inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarCurso.html", {"miFormulario":miFormulario})

@login_required
def eliminarCurso(request, curso_nombre):

      curso = Curso.objects.get(nombre=curso_nombre)
      curso.delete()
      
      #vuelvo al menú
      cursos = Curso.objects.all() #trae todos los cursos

      contexto= {"cursos":cursos} 

      return render(request, "AppCoder/Cursos.html",contexto)








def estudiantes(request):

      estudiantes = Estudiante.objects.all() #trae todos los profesores

      contexto= {"estudiantes":estudiantes} 

      return render(request, "AppCoder/Estudiantes.html",contexto)

@login_required
def agregarEstudiante(request):

      if request.method == 'POST':

            miFormulario = EstudianteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'])

                  estudiante.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= EstudianteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarEstudiante.html", {"miFormulario":miFormulario})

@login_required
def eliminarEstudiante(request, estudiante_nombre):

      estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
      estudiante.delete()
      
      #vuelvo al menú
      estudiantes = Estudiante.objects.all() #trae todos los estudiantes

      contexto= {"estudiantes":estudiantes} 

      return render(request, "AppCoder/Estudiantes.html",contexto)

@login_required
def editarEstudiante(request, estudiante_nombre):

      #Recibe el nombre del estudiante que vamos a modificar
      estudiante = Estudiante.objects.get(nombre=estudiante_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = EstudianteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  estudiante.nombre = informacion['nombre']
                  estudiante.apellido = informacion['apellido']
                  estudiante.email = informacion['email']
                  

                  estudiante.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= EstudianteFormulario(initial={'nombre': estudiante.nombre, 'apellido':estudiante.apellido , 
            'email':estudiante.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarEstudiante.html", {"miFormulario":miFormulario, "estudiante_nombre":estudiante_nombre})









def profesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/Profesores.html",contexto)

@login_required
def agregarProfesor(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/Inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarProfesor.html", {"miFormulario":miFormulario})


@login_required
def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/Profesores.html",contexto)


@login_required
def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})






def buscar(request):

      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      #return HttpResponse(respuesta)






class CursoList(LoginRequiredMixin, ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"
     

#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return render (request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        print(2)
                        return render (request, "AppCoder/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
      print(3)
      return render(request, "AppCoder/login.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "AppCoder/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "AppCoder/registro.html", {"form": form})



@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      print(usuario)
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid: #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppCoder/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




# @login_required
# def agregarAvatar(request):
#       if request.method == 'POST':
#             miFormulario == AvatarFormulario(request.POST, request FILES)
#             if miFormulario.is_valid:
#                   u = User.objects.get(username=request.user)
#                   avatar = Avatar(user=u, imagen=miFormulario.cleaned_data^['imagen'])
#                   avatar.save()
#                   return render(request, "AppCoder/inicio.html")
#             else:
#                   miFormulario =AvatarFormulario()
#             return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario}) 






from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView






urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('about',views.about,name="About"),
    path('Cursos', views.cursos, name="Cursos"),
    path('agregarCurso', views.agregarCurso, name="AgregarCurso"),
    path('eliminarCurso/<curso_nombre>/', views.eliminarCurso, name="EliminarCurso"),
    path('Profesores', views.profesores, name="Profesores"),
    path('agregarProfesor', views.agregarProfesor, name="AgregarProfesor"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    path('Estudiantes', views.estudiantes, name="Estudiantes"),
    path('agregarEstudiante', views.agregarEstudiante, name="AgregarEstudiante"),
    path('eliminarEstudiante/<estudiante_nombre>/', views.eliminarEstudiante, name="EliminarEstudiante"),
    path('editarEstudiante/<estudiante_nombre>/', views.editarEstudiante, name="EditarEstudiante"),
    # path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    
    path('buscar/', views.buscar),
    
    
    
    path('curso/list', views.CursoList.as_view(), name='List'),
       
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),

]


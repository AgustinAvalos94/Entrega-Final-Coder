from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class CursoFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    #extendemos el contenido de el formulario viejo agregando dos campos más
    # last_name: forms.CharField()
    # first_name: forms.CharField()

    class Meta:
        model = User                                               #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'nombre', 'email':'correo','last_name': 'apellido', 'first_name':'nombre'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

# class AvatarForm(forms.Forms):

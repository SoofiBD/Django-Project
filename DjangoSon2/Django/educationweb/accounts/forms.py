from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control' , 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-control' , 'placeholder':'Password'}))

class RegisterForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control' , 'placeholder':'Your Name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control' , 'placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control' , 'placeholder':'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={ 'class':'form-control' , 'placeholder':'E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-control' , 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-control' , 'placeholder':'Repeat Password'}))

    class Meta:
        model = User
        fields = ['name' , 'lastname' , 'username' , 'email' , 'password1' , 'password2']



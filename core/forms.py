from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#create login form
 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeHolder' : 'Your username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeHolder' : 'Your password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

#create sign up form

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeHolder' : 'Your username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeHolder' : 'Your email adresse',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeHolder' : 'Your password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeHolder' : 'Comfirm your password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
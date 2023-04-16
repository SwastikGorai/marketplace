from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget = forms.TextInput(attrs= {
        'placeholder' : 'Your Username',
        'class' : 'w-full py-3 px-4 rounded-2xl'
    }))
    
    email = forms.CharField(widget = forms.EmailInput(attrs= {
        'placeholder' : 'Your Username',
        'class' : 'w-full py-3 px-4 rounded-2xl'
    }))
    
    password1 = forms.CharField(widget = forms.PasswordInput(attrs= {
        'placeholder' : 'Your password',
        'class' : 'w-full py-3 px-4 rounded-2xl'
    }))
    
    password2 = forms.CharField(widget = forms.PasswordInput(attrs= {
        'placeholder' : 'Confirm Password',
        'class' : 'w-full py-3 px-4 rounded-2xl'
    }))
    
    
class LoginForm(AuthenticationForm):
     username = forms.CharField(widget = forms.TextInput(attrs= {
        'placeholder' : 'Your Username',
        'class' : 'w-full py-3 px-4 rounded-2xl'
    }))
     
     password = forms.CharField(widget = forms.PasswordInput(attrs= {
        'placeholder' : 'Confirm Password',
        'class' : 'w-full py-3 px-4 rounded-2xl'
    }))
    
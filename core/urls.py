from django.urls import path
from . import views
from django.contrib.auth import views as authView
from .forms import LoginForm

urlpatterns = [
    path("", views.index, name = "index"),
    path("contact/", views.contact, name= 'contact'),
    path("signup/", views.signup, name= 'signup'),
    path('login/', authView.LoginView.as_view( template_name = 'core/login.html' ,authentication_form = LoginForm), name = 'login'),    
]

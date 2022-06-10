"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from contactos.views import home
from inicio.views import myHomeView, anotherView, tmpView, home, contact
from accounts.views import user_login, user_signup

urlpatterns = [
    path('initial/', myHomeView, name="Pagina de inicio"),
    path('anotherview/', anotherView, name="Another View!"),
    path('tmpView/', tmpView, name="tmp"),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('auth/login/', user_login, name="login"),
    path('auth/signup/', user_signup, name="signup")
]

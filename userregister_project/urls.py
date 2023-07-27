"""userregister_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
from .views import login_view
from .views import admin_password_change_view
from django.contrib import admin
from.views import get_user_security_answer

from django.shortcuts import redirect
urlpatterns=[
     path('', lambda request: redirect('login/')),  
    path('login/', views.login_view, name='login/'),
    path('register/', views.register_view, name='register'),
    path('password_change/', views.password_change_view, name='password_change'),
    path('admin_password_change/', views.admin_password_change_view, name='admin_password_change'),
    path('get_user_security_answer/', views.get_user_security_answer, name='get_user_security_answer'),
     path('admin/', admin.site.urls),
]

# user_management/urls.py
from django.urls import path
from . import views



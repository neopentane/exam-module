"""ExamModule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from myexam import views as e_views
import re
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='myexam/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myexam/logout.html'), name='logout'),
    path('Profile/', e_views.profile, name="profile"),
    re_path(r'^examhall/$', e_views.printo, name='exam'),
    path('result/', e_views.result, name='result'),
    path("signup/", e_views.signup, name='signup')

]

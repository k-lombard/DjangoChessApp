"""django_chess_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from chessapp.views import index, login_view, signup, log_out, account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url('index', index, name='index'),
    url('login', login_view, name='login'),
    url('signup', signup, name='signup'),
    url('log_out', log_out, name='log_out'),
    url('account', account_view, name='account')
]

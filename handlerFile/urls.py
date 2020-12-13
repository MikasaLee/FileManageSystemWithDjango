"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views as handlerfile
app_name = 'handlerfile'

urlpatterns = [
    path('',handlerfile.index,name='index'),
    path('search/',handlerfile.searchfile,name='search'),
    path('addPage/',handlerfile.addPage,name='addPage'),
    path('add/',handlerfile.insertfile,name='add'),
    path('delete/',handlerfile.deletefile,name='delete'),
    path('download/', handlerfile.downloadfile, name='download'),
]

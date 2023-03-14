"""django_api URL Configuration

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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('getdata/', views.getdata),
    path('deldata/<int:id>/', views.deldata),
    path('insdata/', views.insdata),
    path('updata/<int:id>/', views.updata),






# ------------form-----------------.
     path('contact/', views.contact),
     path('deletedata/<int:id>/', views.deletedata),
     path('update/<int:id>/', views.update),
     path('updatedata/<int:id>/', views.updatedata),

]

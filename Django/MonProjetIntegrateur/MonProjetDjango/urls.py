"""
URL configuration for MonProjetDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Etudiant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name = "addandshow"),
    path('connextion/', views.connect, name = "connextion"),
    path('professeur/', views.profs, name = "professeur"),
    path('client/', views.clients, name = "client"),
    path('directeur/', views.directeurs, name = "directeur"),
    path('pre_remplissage/', views.pre_rmp, name='pre_remplissage'),
    path('vue_emploie/', views.v_emploie, name='vue_emploie'),
    path('delete/<int:id>/', views.delete_path, name = "delete_path"),
    path('<int:id>/', views.modifie_path, name = "updatepath"),
    path('base_de_donnee/', views.load_bdd, name='base_de_donnee'),
]


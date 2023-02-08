"""estiamFlix URL Configuration

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
from django.contrib import admin
from listings import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acceuil/',views.acceuil,name='acceuil-serie'),
    path('listes_des_series/', views.listes_des_series, name='listes_des_series'),
    path('serie/<int:id>/',views.seRie, name='serie-detail'),
    path('serie/add/',views.movie_create, name='serie-create'),
    path('serie/<int:id>/modifie/',views.movie_modifie, name='serie-modifie'),
    path('serie/<int:id>/supprime/',views.movie_supprime, name='serie-supprime'),
    path('serie/inscription/',views.inscription, name='serie-inscription'),
    path('serie/acces/',views.acces, name='serie-acces'),
    path('serie/login/',views.login, name='serie-login'),
    path('quitter',views.logOutUse,name='quitter')
]

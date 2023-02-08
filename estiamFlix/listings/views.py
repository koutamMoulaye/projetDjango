from audioop import reverse
from cgitb import html
from multiprocessing import context

from unicodedata import name
from urllib import request
from xmlrpc.client import boolean
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path

from listings.models import movie
from listings.models import movieForm
from django.contrib.auth.forms import UserCreationForm
from .forms import creeUtilistateur
from listings.forms import movieForm
from  django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required
from  django.contrib import messages

#en termes de Python :
# Une vue est une fonction qui accepte un objet HttpRequest comme paramètre et retourne un objetHttpResponse

# ####################vue pour acceuil
def acceuil(request):
    return render(request,'listings/index.html')
# ####################vue listes des series
def listes_des_series(request):
    movies=movie.objects.all()
    return render(request,
    'listings/listes_des_series.html',
    {'movies': movies})

# ####################vue pour serie  en detail
def seRie(request, id):
    moviess= movie.objects.get(id=id)# nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
          'listings/serie.html',
          {'moviess': moviess}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

# ####################vue pour creation des series
@login_required(login_url='serie/add/')
def movie_create(request):
    if request.method == 'POST':
        form = movieForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            movie = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('serie-detail', movie.id)
    else:
        form = movieForm()
    return render(request,
            'listings/movie_create.html',
            {'form': form})

# ####################vue pour modidication des series

def movie_modifie(request, id):
    moviesss = movie.objects.get(id=id)

    if request.method == 'POST':
        form = movieForm(request.POST, instance=moviesss)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('serie-detail', moviesss.id)
    else:
        form = movieForm(instance=moviesss)

    return render(request,
                'listings/movie_modifie.html',
                {'form': form})

# ####################vue pour supprimer serie desirée

def movie_supprime(request, id):
    moviessss = movie.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        moviessss.delete()
        # rediriger vers la liste des groupes
        return redirect('listes_des_series')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/movie_supprime.html',
                    {'moviessss': moviessss})

# ####################vue pour inscription

def inscription (request):
    form2=creeUtilistateur()
    if request.method == 'POST':
     form2=creeUtilistateur(request.POST)
     if form2.is_valid():
        form2.save()
        user=form2.cleaned_data.get('username')
        messages.success(request,'Acccount is create for '+ user +'!!')
        return redirect('serie-acces')
    context ={'form2':form2}
    return render(request,'listings/inscription.html',context)

# ####################vue pour inscription

def acces (request):
    context ={}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request)
            return redirect('acceuil-serie')
        else:
            messages.info(request,"user or password don't exist")
    return render(request,'listings/acces.html')

def logOutUse(request):
    logout(request)
    return redirect('serie-acces')



def login (request): 
  
    return render(request,'listings/login.html')

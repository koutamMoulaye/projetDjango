from django.contrib import admin
from listings.models import movie

# Register your models here.


class movieadmin(admin.ModelAdmin):
    list_display=('titre', 'description', 'realisateur','annee_de_sortie', 'nombre_episode')# liste les champs que nous voulons sur 
# l'affichage de la liste

admin.site.register(movie, movieadmin) # nous modifions cette ligne, en ajoutant un deuxième argument

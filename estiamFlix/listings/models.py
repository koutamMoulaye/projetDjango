from turtle import title
from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models
# Create your models here.
class serie (models.Model):
    titre = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    realisateur = models.fields.CharField(max_length=100)
    annee_de_sortie = models.IntegerField()
    nombre_episode = models.IntegerField()

class movie (models.Model):
    titre = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    realisateur = models.fields.CharField(max_length=100)
    annee_de_sortie = models.IntegerField()
    nombre_episode = models.IntegerField()

    def __str__(self):
        return f'{self.titre}'

class movieForm (forms.Form):
    titre =forms.fields.CharField(max_length=100)
    description = forms.fields.CharField(max_length=100)
    realisateur = forms.fields.CharField(max_length=100)
    annee_de_sortie = forms.IntegerField()
    nombre_episode = forms.IntegerField()
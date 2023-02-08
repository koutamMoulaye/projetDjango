from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from listings.models import movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class movieForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = '__all__'

class creeUtilistateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
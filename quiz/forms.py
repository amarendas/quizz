from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class AddQ(forms.Form):
#     question=forms.CharField(max_length=1000)
#     opt1=forms.CharField(max_length=500)
#     opt2=forms.CharField(max_length=500)
#     opt3=forms.CharField(max_length=500)
#     opt4=forms.CharField(max_length=500)
#     Answer=forms.CharField(widget=forms.Textarea)

from curses import meta
from dataclasses import fields
from django.forms import ModelForm
from .models import Quiz_Question,Author, Subject


# ceate the form calss
class AddQ (ModelForm):
    extra= forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 2}))
    #answer= forms.CharField(widget=forms.Textarea(attrs={'cols': 1, 'rows': 1}))
    class Meta:
        model=Quiz_Question
        fields=['difficulty_level', 'question','opt1','opt2', 'opt3', 'opt4','answer','extra','subject',]
        
class AddS (ModelForm):
    
    class Meta:
        model=Subject
        fields=[ 'name',]
       
       
  
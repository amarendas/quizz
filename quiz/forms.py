# from django import forms
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
    class Meta:
        model=Quiz_Question
        fields=[ 'question','opt1','opt2', 'opt3', 'opt4','answer','subject']
        
class AddS (ModelForm):
    class Meta:
        model=Subject
        fields=[ 'name',]
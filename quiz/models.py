
from pickle import FALSE
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
LEVEL_CHOICE=[
    ('BASIC','BASIC'),
    ('INTR','INTERMEDIAT'),
    ('ADV', 'ADVANCED'),
    ('EXPERT','EXPERT'),
]
class Quiz_Question(models.Model):
    question=models.CharField(max_length=500)
    opt1=models.CharField(max_length=200,null=True)
    opt2=models.CharField(max_length=200,null=True)
    opt3=models.CharField(max_length=200,null=True)
    opt4=models.CharField(max_length=200,null=True)
    answer=models.CharField(max_length=200)
    extra=models.TextField(max_length=500, 
                           help_text= 'Some extra interesting  info on the answer',null=True)
    difficulty_level=models.CharField( max_length=6,
        choices=LEVEL_CHOICE,
        blank=FALSE,
        default='BASIC',
        help_text='Level of Dificulty to be juged by the author',
    )
    subject=models.ForeignKey('Subject', on_delete=models.SET_NULL,null=True)
    Author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.question
    
class Author(models.Model):
    name=models.CharField(max_length=30)
    
    Division=models.CharField(max_length=30)
    phone=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(20000),
                                  MaxValueValidator(29999)])
    email=models.EmailField(max_length=30,null=True)
    def __str__(self):
        return self.name + "  (" +self.Division +")"
    
class Subject(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    
    
    
    

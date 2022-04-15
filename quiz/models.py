
from pickle import FALSE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
LEVEL_CHOICE=[
    ('B','BASIC'),
    ('I','INTERMEDIAT'),
    ('A', 'ADVANCED'),
    ('E','EXPERT'),
]
class Quiz_Question(models.Model):
    question=models.CharField(max_length=500)
    opt1=models.CharField(max_length=200,null=True)
    opt2=models.CharField(max_length=200,null=True)
    opt3=models.CharField(max_length=200,null=True)
    opt4=models.CharField(max_length=200,null=True)
    answer=models.TextField(max_length=200)
    difficulty_level=models.CharField(
        max_length=1,
        choices=LEVEL_CHOICE,
        blank=FALSE,
        default='B',
        help_text='Level of Dificulty',
    )
    subject=models.ForeignKey('Subject', on_delete=models.SET_NULL,null=True)
    Author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    
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
    
    
    
    
    

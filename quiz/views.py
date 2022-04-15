from django.shortcuts import render
from .models import Quiz_Question,Author, Subject

def index(request):
    question_list =Quiz_Question.objects.all()
    q_nos=Quiz_Question.objects.count()
    context={'q_list':question_list,"q_nos":q_nos}
    return render(request,'index.html', context)

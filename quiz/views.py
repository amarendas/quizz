from django.shortcuts import render
from .models import Quiz_Question,Author, Subject

def index(request):
    question_list =Quiz_Question.objects.all()
    topic_list=Subject.objects.all()
    
    q_nos=Quiz_Question.objects.count()
    context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list}
    return render(request,'index.html', context)

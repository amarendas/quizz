from django.shortcuts import render
from .models import Quiz_Question,Author, Subject

def index(request):
    question_list =Quiz_Question.objects.all()
    context={'q_list':question_list}
    return render(request,'index.html', context)

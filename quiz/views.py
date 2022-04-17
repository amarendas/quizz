from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from .models import Quiz_Question,Author, Subject
from .forms import AddQ, AddS
from django.contrib import messages

def index(request):
    question_list =Quiz_Question.objects.all()
    topic_list=Subject.objects.all()
    
    q_nos=Quiz_Question.objects.count()
    context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list}
    return render(request,'index.html', context)

def filtered_by_topic(request,pk):
    sub=Subject.objects.get(pk=pk).name
    question_list =Quiz_Question.objects.filter(subject__name=sub)
    topic_list=Subject.objects.all()
    
    q_nos=question_list.count()
    context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list}
    return render(request,'index.html', context)


def addQuestion(request):
    topic_list=Subject.objects.all()
    q_nos=Quiz_Question.objects.count()
    if request.method=='POST':
        form=AddQ(request.POST)
        if form.is_valid():
            # Process Data
            form.save()
            messages.success(request, ('Your question was successfully added!'))
            cd=form.cleaned_data
            print(cd)
            return redirect(reverse('quiz'))
        else:
            messages.error(request, 'Error saving form')
    else:
        form=AddQ()
    context={'topics':topic_list,'form':form,"q_nos":q_nos,}
    return render (request,'addMyQuestion.html',context)


def addSubject(request):
    topic_list=Subject.objects.all()
    q_nos=Quiz_Question.objects.count()
    if request.method=='POST':
        form=AddS(request.POST)
        if form.is_valid():
            # Process Data
            form.save()
            messages.success(request, ('Your question was successfully added!'))
            cd=form.cleaned_data
            print(cd)
            return redirect(reverse('quiz'))
        else:
            messages.error(request, 'Error saving form')
    else:
        form=AddS()
        print(form)
    context={'topics':topic_list,'form':form,"q_nos":q_nos,}
    return render (request,'addSubject.html',context)
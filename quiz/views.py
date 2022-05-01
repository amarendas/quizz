from django.urls import reverse

from django.http import Http404
from django.shortcuts import redirect, render,get_object_or_404

from .models import Quiz_Question,Author, Subject,User
from .forms import AddQ, AddS
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.user.is_superuser:  
        authors=User.objects.all()  
        username=request.user.username
        question_list =Quiz_Question.objects.all()
        topic_list=Subject.objects.all()
        q_nos=question_list.count()
        context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list,'authors':authors}
        return render(request,'index.html', context)
    else:
        return redirect(allMyQuistions)

def allMyQuistions(request):    
    username=request.user.username
    question_list =Quiz_Question.objects.filter(Author__username=username)
    topic_list=Subject.objects.all()
    q_nos=question_list.count()
    context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list}
    return render(request,'index.html', context)

def filtered_by_topic(request,pk):
    username=request.user.username
    question_list =Quiz_Question.objects.filter(Author__username=username)
    sub=Subject.objects.get(pk=pk).name
    question_list =question_list.filter(subject__name=sub)
    topic_list=Subject.objects.all()
    
    q_nos=question_list.count()
    context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list}
    return render(request,'index.html', context)


@login_required
def quiz_detail_view(request,pk):
    try:
        q = Quiz_Question.objects.get(pk=pk)
    except q.DoesNotExist:
        raise Http404('Question does not exist')
    if request.method=='POST':
        form=AddQ(request.POST,request.FILES)
        if form.is_valid():
            # Process Data
            f=form.save(commit=False) # Create the model instance with the form
            f.Author=q.Author #  Not required as old author get modified if super user changes the question.
            f.pk=q.id # Now change the model instant filds
            f.save() # save the object to data base
            messages.success(request, ('Your question was successfully added!'))
            cd=form.cleaned_data
            return redirect(reverse('quiz'))
        else:
            messages.error(request, 'Error saving form')
    else:
        form=AddQ(instance=q)
        
    topic_list=Subject.objects.all()
    q_nos=Quiz_Question.objects.count()
    context={'q':q,'form': form,"q_nos":q_nos,'topics':topic_list}
    return render(request, 'question_detail.html', context)

@login_required
def addQuestion(request):
    topic_list=Subject.objects.all()
    q_nos=Quiz_Question.objects.count()
    if request.method=='POST':
        form=AddQ(request.POST, request.FILES)
        if form.is_valid():
            # Process Data
            f=form.save(commit=False) # Create the model instance with the form
            f.Author=request.user  # Now change the model instant filds
            print(f.Author)         
            f.save() # save the object to data base
            messages.success(request, ('Your question was successfully added!'))
            cd=form.cleaned_data
            
            return redirect(reverse('quiz'))
        else:
            messages.error(request, 'Error saving form')
    else:
        form=AddQ()
    context={'topics':topic_list,'form':form,"q_nos":q_nos,}
    return render (request,'addMyQuestion.html',context)

@login_required
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

@login_required
def delete_question(request,pk):
    q=Quiz_Question.objects.get(id=pk)
    q.delete()
    return redirect(index)

@login_required
def list_by_user(request,pk):
    username=User.objects.get(pk=pk)
    question_list =Quiz_Question.objects.filter(Author__username=username)
    q_nos=question_list.count()
    topic_list=Subject.objects.all()
    context={'q_list':question_list,"q_nos":q_nos,'topics':topic_list}
    return render(request,'index.html', context)
    
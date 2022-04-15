from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Quiz_Question,Author, Subject

def index(request):
    return HttpResponse("Hi, Hello APD")
"""tutoria1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from quiz import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.allMyQuistions,name='quiz'),
    path('allQuestions',views.index,name='allQ'),
    path('addQ',views.addQuestion,name='addQ'),
    path('addS',views.addSubject,name='addS'),
    path('quiz_by_topic/<int:pk>',views.filtered_by_topic,name='quiz_by_topic'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('quiz/<int:pk>', views.quiz_detail_view, name='quiz-detail'),
    path('delete_question/<int:pk>',views.delete_question,name='delete_question'),
    path('list_by_auth/<int:pk>', views.list_by_user,name='list_by_user'),
    
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
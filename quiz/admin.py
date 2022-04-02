from django.contrib import admin
from .models import Quiz_Question,Author, Subject
# Register your models here.
admin.site.register(Quiz_Question)
admin.site.register(Author)
admin.site.register(Subject)

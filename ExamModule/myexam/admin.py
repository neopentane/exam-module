from django.contrib import admin
from .models import Modules, Student, Exam, Question, Choice

admin.site.register(Modules)
admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.

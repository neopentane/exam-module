from django.shortcuts import render
from .models import Modules,Student,Exam,Question,Choice
# Create your views here.
def profile(requests):
    c_user=requests.user
    c_student=c_user.student
    #c_student=c_user.roll_no
    a_module=c_student.exam_modules
    a_exams=Exam.objects.filter(module=a_module)
    context={
    "exams":a_exams

    }
    return render(requests,'myexam/profile.html',context)

def printo(requests):
	if requests.method=='GET':
		now_exam=requests.GET.get('exam')
		c_exam=Exam.objects.filter(exam=now_exam).first()
		c_questions=Question.objects.filter(exam=c_exam)
		context={
            "questions":c_questions
        }
	return render(requests,'myexam/exam.html',context)

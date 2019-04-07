from django.shortcuts import render, redirect
from .models import Modules, Student, Exam, Question, Choice
import random
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegForm
# Create your views here.


def profile(request):
    c_user = request.user
    c_student = c_user.student
    # c_student=c_user.roll_no
    a_module = c_student.exam_modules
    a_exams = Exam.objects.filter(module=a_module)
    context = {
        "exams": a_exams

    }
    return render(request, 'myexam/profile.html', context)


def printo(request):
    if request.method == 'GET':
        now_exam = request.GET.get('exam')
        c_exam = Exam.objects.filter(exam=now_exam).first()
        c_questions = Question.objects.filter(exam=c_exam)
        context = {
            "questions": c_questions
        }
    return render(request, 'myexam/exam.html', context)


def calresult(request):
    if request.method == "POST":
        answer = request.POST.get("h-type")
        score = 0
        for i, j in zip(c_exam.answer, answer):
            if(i == j):
                score += 1
            return score
    redirect('profile')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form2 = StudentRegForm(request.POST)
        if form.is_valid() and form2.is_valid:
            c_user = form.save()
            c_student = form2.save(commit=False)
            c_student.roll_no = c_user
            c_student.save()
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
        form2 = StudentRegForm()
    return render(request, 'myexam/signup.html', {"form": form, "form2": form2})


def result(request):
    t = []
    for i in range(0, 5):
        t.append(random.randint(1, 4))
    context = {"ans": t}
    if request.method == "POST":
        h_type = request.POST.get('h-type')
        res = random.randint(1, 4)
        context = {
            "ans": t,
        }
    return render(request, 'myexam/result.html', context)

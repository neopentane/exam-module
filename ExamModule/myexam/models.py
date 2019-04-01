from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Modules(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Student(models.Model):
    roll_no=models.OneToOneField(User,on_delete=models.CASCADE)
    exam_modules=models.ForeignKey(Modules,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.roll_no.username}'

class Exam(models.Model):
    exam=models.CharField(max_length=30)
    module=models.ForeignKey(Modules,on_delete=models.CASCADE)
    def __str__(self):
        return self.exam

class Question(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    question_no = models.IntegerField("question_no")
    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("exam", "question"),
            # no duplicated position per question
            ("exam", "question_no")
        ]
        ordering = ("question_no",)
    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey("Question", related_name="choices",on_delete=models.CASCADE)
    choice = models.CharField("Choice", max_length=50)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"),
            # no duplicated position per question
            ("question", "position")
        ]
        ordering = ("position",)

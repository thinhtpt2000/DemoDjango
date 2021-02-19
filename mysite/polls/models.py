from django.db import models

# Create your models here.
# Ở đây chứa/định nghĩa các models/thực thể khi dùng với DB, ví dụ như Student

class Question(models.Model):
    question_text  = models.CharField(max_length=200)
    time_public = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
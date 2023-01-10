from django.db import models
from django.contrib.auth.models import User # django.contrib.auth 앱이 제공하는 사용자 모델

# Create your models here.

class Question(models.Model): # DTO 역할?
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') 
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')


    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 기존 모델 속성 연결
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

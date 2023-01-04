from django.db import models

# Create your models here.

class Question(models.Model): # DTO 역할?
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 기존 모델 속성 연결
    content = models.TextField()
    create_date = models.DateTimeField()
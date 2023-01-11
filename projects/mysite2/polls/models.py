import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model): # `django.db.models.Model`의 하위 클래스
    question_text = models.CharField(max_length=200) # 필드
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# get은 QuerySet이 아니라 1개 리턴
# q.choice_set.all() : foreign이므로 Choice접근 가능
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
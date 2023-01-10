from django import forms
from pybo.models import Question, Answer
# 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해
# 필수 파라미터의 값이 누락되지 않았는지, 파라미터의 형식은 적절한지 등을 검증할 목적
class QuestionForm(forms.ModelForm): # 연결된 모델의 데이터를 저장할수 있는 폼, 필요한 항목만 사용하기 위해 모델 생성.
    class Meta: # 필수
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = { # 자동으로 생성되는 HTML코드(form.as_p)에서 부트스트랩 속성 추가
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }
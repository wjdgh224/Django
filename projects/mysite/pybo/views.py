from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list} # 템플릿과 파이썬의 연결, 변수 전달
    return render(request, 'pybo/question_list.html', context) # question_list데이터 html(템플릿)에 적용하여 생성 후 리턴

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request): # POST일 때 request는 데이터를 가진다.
    if request.method == 'POST':
        form = QuestionForm(request.POST) # 인수에 subject, content값이 QuestionForm 속성에 대입
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form' : form})
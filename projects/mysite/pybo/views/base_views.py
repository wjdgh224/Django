from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


from ..models import Question

def index(request):
    page = request.GET.get('page', '1') # ?page=1(default) 쿼리스트링
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page) # 해당 페이지에 해당되는 페이징 객체 생성
    context = {'question_list' : page_obj, 'page': page, 'kw': kw} # 템플릿과 파이썬의 연결, 변수 전달
    return render(request, 'pybo/question_list.html', context) # question_list데이터 html(템플릿)에 적용하여 생성 후 리턴

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

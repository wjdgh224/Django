from this import d
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
#models, 즉 데이터베이스에는 pk, id라는 구별 가능한 값이 적용됨

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {"todos": todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_post(request): # post에서 요청 시 실행 후 모델 저장
    if request.method == 'POST':
        form = TodoForm(request.POST) # post요청시(전송, 클릭) 모든(작성한) 데이터 TodoForm형태로
        if form.is_valid():
            todo = form.save(commit=False) # form으로 부터 데이터 받아와
            todo.save() # 데이터 베이스 저장
            return redirect('todo_list')
    else: # 웹 브라우저에서 페이지 접속 요청은 Get
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request, pk): # 개별적 데이터 불러오기(상세보기, 수정)은 pk필요
    todo =  Todo.objects.get(id=pk) # 선택한 목록, detail과 같음
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo) # instance로 todo변수로 한 목록을 구분한 정보를 줘야 같은 데이터 베이스에 적용됨
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo) # form형식에 선택한 목록(todo 값) 적용
    return render(request, 'todo/todo_post.html', {'form': form}) 
    # POST가 오지 않으면, 즉 아무 것도 하지 않으면 저장된 데이터 형식(form)의 todo_post를 불러온다
    # instance ------> 수정 대상이 될 데이터 설정, 설정하지 않으면 생성시 또다른 목록이 생성
def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones': dones})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True # todo 데이터 접근 및 수정
    todo.save() # 저장
    return redirect('todo_list')
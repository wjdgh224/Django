from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
# 데이터(model)를 가져와서 render를 이용해 화면(template)과 연결시키긴다.
def photo_list(request):
    photos = Photo.objects.all() # models 데이터에서 모든 Photo 불러오기
    return render(request, 'photo/photo_list.html', {'photos':photos}) # html 화면 출력 및 데이터 전달

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk) # 데이터베이스에 pk값(ID값, 구분값)에 해당하는 객체 찾기
    return render(request, 'photo/photo_detail.html', {'photo':photo}) # 해당 객체 출력 및 데이터 전달

def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST) # forms 형식의 객체 가져오기
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk) # 데이터베이스에 저장 후 화면 출력
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_post.html', {'form': form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk) # 저장된 객체 pk로 찾고
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo) # instance로 대상 찾기
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form': form})
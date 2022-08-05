from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'), # 홈페이지에 photo_list출력
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/new/', views.photo_post, name='photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    # (새로운 주소 형식, view 즉 template과 model을 이어줄 함수(view) 호출)
]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), # LoginView는 원래 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다
    # 로그인이 성공하면 django.contrib.auth 패키지는 디폴트로 /accounts/profile/ 이라는 URL로 이동
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
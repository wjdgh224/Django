"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

#from pybo import views

# url입력시 가장 먼저 실행 후 views.py와 매핑
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pybo/', views.index), 
    path('pybo/', include('pybo.urls')), # pybo와 관련된 처리를 하는 urls따로 만듦. config에 특정 앱에 대한 매핑을 일일이 하지 않고 한번에 처리
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]

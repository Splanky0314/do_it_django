from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # views.py에 있는 index() 함수 실행
]
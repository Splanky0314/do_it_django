from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # views.py에 있는 index() 함수 실행
    path('<int:pk>/', views.PostDetail.as_view())
]
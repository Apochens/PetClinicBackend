from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuizAPIView.as_view()),
    path('question/', views.QuestionAPIView.as_view()),
]
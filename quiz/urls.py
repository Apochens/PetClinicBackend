from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuizAPIView.as_view()),
    path('<int:quiz_id>', views.get_single_quiz),
    path('question/', views.QuestionAPIView.as_view()),
    path('question/<str:question_type>/<int:question_id>/', views.get_single_question)
]
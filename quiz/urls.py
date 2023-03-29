from django.urls import path
from . import views


urlpatterns = [
    # quiz
    path('', views.QuizAPIView.as_view()),
    path('<int:quiz_id>/', views.get_single_quiz),

    # question
    path('question/', views.QuestionAPIView.as_view()),
    path('question/init/', views.question_init),
    path('question/<str:question_type>/<int:question_id>/', views.get_single_question),

    # score
    path('score/', views.submit_quiz_result),
    path('score/user/<int:user_id>', views.get_quiz_result_by_user),
    path('score/quiz/<int:quiz_id>', views.get_quiz_result_by_quiz),
]
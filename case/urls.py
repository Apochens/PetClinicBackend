from django.urls import path

from . import views

urlpatterns = [
    path('', views.CaseView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('checkup/', views.CheckView.as_view())
]

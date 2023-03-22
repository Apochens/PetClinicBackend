from django.urls import path

from . import views

urlpatterns = [
    # case
    path('', views.CaseView.as_view()),
    path('number/<str:case_number>/', views.get_single_case_by_number),
    path('name/<str:disease_name>/', views.get_cases_by_name),
    # category list
    path('category/', views.CategoryView.as_view()),
    # checkup
    path('checkup/', views.CheckView.as_view()),
    path('checkup/<str:case_number>/', views.get_checkups_by_number),
    # test for upload files
    path('upload/', views.test_upload),
]

from django.urls import path
from . import views

urlpatterns = [
    path('department/data/', views.DepartmentAPIView.init),
    path('department/', views.DepartmentAPIView.as_view()),
    path('department/<int:id>/', views.DepartmentAPISingleView.as_view()),
    path('medicine/data/', views.MedicineAPIView.init),
    path('medicine/', views.MedicineAPIView.as_view()),
    path('medicine/<int:id>/', views.MedicineAPISingleView.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('department/data/', views.DepartmentAPIView.init),
    path('department/instrumentation/<int:id>/', views.DepartmentAPIView.instrumentation),
    path('department/checkup/<int:id>/', views.DepartmentAPIView.checkup),
    path('department/', views.DepartmentAPIView.as_view()),
    path('department/<int:id>/', views.DepartmentAPISingleView.as_view()),
    path('medicine/data/', views.MedicineAPIView.init),
    path('medicine/', views.MedicineAPIView.as_view()),
    path('medicine/<int:id>/', views.MedicineAPISingleView.as_view()),
    path('instrumentation/data/', views.InstrumentationAPIView.init),
    path('instrumentation/', views.InstrumentationAPIView.as_view()),
    path('instrumentation/<int:id>/', views.InstrumentationAPISingleView.as_view()),
    path('checkup/data/', views.CheckupAPIView.init),
    path('checkup/', views.CheckupAPIView.as_view()),
    path('checkup/<int:id>/', views.CheckupAPISingleView.as_view()),
]
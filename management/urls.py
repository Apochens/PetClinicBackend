from django.urls import path
from . import views

urlpatterns = [
    path('department/data/', views.DepartmentAPIView.init),
    path('department/instrumentation/<str:id>/', views.DepartmentAPIView.instrumentation),
    path('department/checkup/<str:id>/', views.DepartmentAPIView.checkup),
    path('department/', views.DepartmentAPIView.as_view()),
    path('department/<str:id>/', views.DepartmentAPISingleView.as_view()),
    path('medicine/data/', views.MedicineAPIView.init),
    path('medicine/', views.MedicineAPIView.as_view()),
    path('medicine/<str:id>/', views.MedicineAPISingleView.as_view()),
    path('instrumentation/data/', views.InstrumentationAPIView.init),
    path('instrumentation/', views.InstrumentationAPIView.as_view()),
    path('instrumentation/<str:id>/', views.InstrumentationAPISingleView.as_view()),
    path('checkup/data/', views.CheckupAPIView.init),
    path('checkup/', views.CheckupAPIView.as_view()),
    path('checkup/<str:id>/', views.CheckupAPISingleView.as_view()),
    path('hospitalization/data/', views.HospitalizationAPIView.init),
    path('hospitalization/', views.HospitalizationAPIView.as_view()),
    path('hospitalization/<str:id>/', views.HospitalizationAPISingleView.as_view()),
]
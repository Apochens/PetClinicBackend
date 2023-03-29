from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoleAPIView.as_view()),
    path('init/', views.role_init),
    path('<int:role_id>/', views.get_role_by_id)
]

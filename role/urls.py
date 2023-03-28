from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoleAPIView.as_view()),
    path('<str:role_id>', views.get_role_by_id)
]

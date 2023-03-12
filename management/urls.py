from django.urls import path
from . import views

urlpatterns = [
    path('department/<int:id>', views.get),
]
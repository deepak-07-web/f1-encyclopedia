from django.urls import path
from . import views

urlpatterns = [
    path('', views.circuit_list, name='circuit_list'),
    path('<int:pk>/', views.circuit_detail, name='circuit_detail'),
]
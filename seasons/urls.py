from django.urls import path
from . import views

urlpatterns = [
    path('', views.season_list, name='season_list'),
    path('<int:pk>/', views.season_detail, name='season_detail'),
]
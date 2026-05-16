from django.urls import path
from . import views

urlpatterns = [
    path('', views.legend_list, name='legend_list'),
]

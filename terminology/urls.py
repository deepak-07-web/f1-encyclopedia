from django.urls import path
from . import views

urlpatterns = [
    path('', views.terminology_list, name='terminology_list'),
]
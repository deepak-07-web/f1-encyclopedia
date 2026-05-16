from django.urls import path
from . import views

urlpatterns = [
    path('', views.tyre_list, name='tyre_list'),
]
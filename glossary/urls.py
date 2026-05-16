from django.urls import path
from . import views

urlpatterns = [
    path('', views.glossary_list, name='glossary_list'),
]
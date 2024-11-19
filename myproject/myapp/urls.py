# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.string_input_view, name='string_input'),
]

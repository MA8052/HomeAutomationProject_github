from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeLight, name='HomeLight'), 
]
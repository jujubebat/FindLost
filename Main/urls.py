from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('LabPage', views.LabPage, name='LabPage'),
]

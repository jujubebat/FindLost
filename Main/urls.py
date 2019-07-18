from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('LostItems', views.LostItems, name='LostItems'),
    path('LabPage', views.LabPage, name='LabPage'),
]

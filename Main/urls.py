from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('FindLost', views.FindLost, name='FindLost'),
    path('FindLost/<int:pk>', views.ItemDetail, name='ItemDetail'),
    path('LabPage', views.LabPage, name='LabPage'),
]

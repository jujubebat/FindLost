from django.shortcuts import render
from .models import LostItems

def HomePage(request):
    return render(request, 'HomePage.html', {})

def LostItems(request):
    return render(request, 'LostItems.html', {})

def LabPage(request):
    data = LostItems.objects.all()
    return render(request, 'LabPage.html', {'data' : data})


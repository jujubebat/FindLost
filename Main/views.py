from django.shortcuts import render, get_object_or_404
from .models import LostItems
from django.core.paginator import Paginator

def HomePage(request):
    return render(request, 'HomePage.html', {})

def FindLost(request):
    data = LostItems.objects.all()
    paginator = Paginator(data, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'FindLost.html', {'items': items})

def ItemDetail(request, pk):
    item = get_object_or_404(LostItems, pk=pk)
    return render(request, 'ItemDetail.html', {'item' : item})

def LabPage(request):
    data = LostItems.objects.all()
    paginator = Paginator(data,10)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'LabPage.html', {'items' : items})


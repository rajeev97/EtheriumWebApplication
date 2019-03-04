from django.shortcuts import render
from django.views.generic import ListView
from .models import Item
import requests

class ItemListView(ListView):
    model=Item
    queryset=Item.objects.all()


def home(request):
    return render(request,"Feedpage.html")
def login(request):
    return render(request,"Login.html")

from django.shortcuts import render, redirect
from .models import Fashion

def home(request):
    fashion_items = Fashion.objects.all()
    return render(request, 'index.html', {'fashion_items': fashion_items})



# Create your views here.

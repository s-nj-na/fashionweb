from django.shortcuts import render, redirect
from .models import Fashion

def home(request):
    fashion_items = Fashion.objects.all()
    return render(request, 'index.html', {'fashion_items': fashion_items})

def redirect_to_bootstrap(request):
    return redirect('/bootstrap/')

# Create your views here.

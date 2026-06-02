from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Fashion

def order(request):
    fashion_items = Fashion.objects.all()
    return render(request, 'order.html', {'fashion_items': fashion_items})


def home(request):
    fashion_items = Fashion.objects.all()
    return render(request, 'index.html', {'fashion_items': fashion_items})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth_logout(request)

    return redirect('home')

@login_required
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        fashion = Fashion(title=title, description=description, price=price, image=image)
        fashion.save()

        return redirect('home')
    return render(request, 'add_product.html')

@login_required
def edit_product(request, id):
    fashion = Fashion.objects.get(id=id)
    if request.method == 'POST':
        fashion.title = request.POST.get('title')
        fashion.description = request.POST.get('description')
        fashion.price = request.POST.get('price')
        if request.FILES.get('image'):
            fashion.image = request.FILES.get('image')
        fashion.save()
        return redirect('home')
    return render(request, 'edit_product.html', {'fashion': fashion})

@login_required
def delete_product(request, id):
    fashion = Fashion.objects.get(id=id)
    if request.method == 'POST':
        fashion.delete()
        return redirect('home')
    return render(request, 'delete_product.html', {'fashion': fashion})
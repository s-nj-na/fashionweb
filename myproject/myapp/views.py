from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Fashion, Task

class EmployeeRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

def order(request):
    fashion_items = Fashion.objects.all()
    return render(request, 'order.html', {'fashion_items': fashion_items})


def home(request):
    fashion_items = Fashion.objects.all()
    return render(request, 'index.html', {'fashion_items': fashion_items})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role')

        if form.is_valid():
            user = form.save(commit=False)
            
            if role == 'employee':
                user.is_staff = True
                user.is_active = False
                user.save()
                return redirect('pending_approval')
            else:
                user.is_staff = False
                user.is_active = True
                user.save()
                auth_login(request, user)
                return redirect('task_list')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

class PendingApprovalView(TemplateView):
    template_name = 'pending.html'

class RoleBasedLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('task_list')

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

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, EmployeeRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin, EmployeeRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, EmployeeRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
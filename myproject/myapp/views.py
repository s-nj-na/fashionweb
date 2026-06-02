from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Fashion
from .forms import FashionForm

from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TaskListView(LoginRequiredMixin,ListView):
    model=Fashion
    template_name='hello'
    context_object_name='fashions_list'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['task_form']=FashionForm()
         return context
    
    def post(self,request,*args,**kwargs):
      form=FashionForm(request.POST)
      if form.is_valid():
            form.save()
            return redirect('hello')
      
      return self.get(request,*args,**kwargs)

class TaskDetailView(LoginRequiredMixin,DetailView):
    model=Fashion 
    template_name='fashion_details.html'   
    context_object_name='fashion'








def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hello')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
# Create your views here.

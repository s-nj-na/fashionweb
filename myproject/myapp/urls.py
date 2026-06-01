from django.urls import path
from . import views
from .views import TaskListView,TaskDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", TaskListView.as_view(), name="hello"),
    path('hello/', TaskListView.as_view(), name='base'),

    
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    #login and logout urls
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #signup url
    path('signup/', views.signup, name='signup'),
]
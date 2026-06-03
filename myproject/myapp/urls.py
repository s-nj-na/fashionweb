from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.RoleBasedLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('pending/', views.PendingApprovalView.as_view(), name='pending_approval'),
]
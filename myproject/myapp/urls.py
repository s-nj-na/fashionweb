from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('order/', views.order, name='order'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
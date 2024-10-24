from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('add/', views.add_food, name='add_food'),
    path('edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'),
    path('login/', views.login, name='login'),   
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm, RegistrationForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods, 'current_year': timezone.now().year})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.view_count += 1
    food.save()
    return render(request, 'food_detail.html', {'food': food})

@login_required
def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.created_by = request.user
            food.save()
            messages.success(request, 'Food item added successfully.')
            return redirect('menu:food_list')
    else:
        form = FoodForm()
    return render(request, 'food_form.html', {'form': form})

@login_required
def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if food.created_by != request.user and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit this food item.')
        return redirect('menu:food_list')
    
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item updated successfully.')
            return redirect('menu:food_list')
    else:
        form = FoodForm(instance=food)
    
    return render(request, 'food_form.html', {'form': form})

@login_required
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if food.created_by != request.user and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete this food item.')
        return redirect('menu:food_list')

    if request.method == "POST":
        food.delete()
        messages.success(request, 'Food item deleted successfully.')
        return redirect('menu:food_list')

    return render(request, 'food_confirm_delete.html', {'food': food})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('menu:food_list')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('menu:food_list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('menu:login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

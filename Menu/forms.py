from django import forms
from django.contrib.auth.models import User
from .models import Food, Comment, FoodType  

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'name', 'ingredients', 'price', 'image', 'preparation_time']
        widgets = {
            'food_type': forms.Select(attrs={
                'class': 'form-control',
                'aria-label': 'Food Type',
                'required': True,
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter food name',
                'aria-label': 'Food Name',
                'required': True,
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter ingredients',
                'aria-label': 'Ingredients',
                'required': True,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'aria-label': 'Price',
                'required': True,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'aria-label': 'Food Image',
            }),
            'preparation_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preparation time in minutes',
                'aria-label': 'Preparation Time',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['food_type'].queryset = FoodType.objects.all()

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'aria-label': 'Username',
            'required': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'aria-label': 'Password',
            'required': True,
        })
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password',
        'aria-label': 'Password',
        'required': True,
    }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm your password',
        'aria-label': 'Confirm Password',
        'required': True,
    }), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
                'aria-label': 'Username',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'aria-label': 'Email',
                'required': True,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add a comment...',
                'aria-label': 'Comment Content',
                'required': True,
            }),
        }

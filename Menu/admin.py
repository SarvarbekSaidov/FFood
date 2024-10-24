from django.contrib import admin
from .models import Food, FoodType
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'food_type', 'view_count')
    search_fields = ('name',)
    list_filter = ('food_type',)

class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Food, FoodAdmin)
admin.site.register(FoodType, FoodTypeAdmin)

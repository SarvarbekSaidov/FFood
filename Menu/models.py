from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class FoodType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Food Type Name")

    class Meta:
        verbose_name_plural = "Food Types"
        permissions = [
            ("can_add_foodtype", "Can add food type"),
            ("can_edit_foodtype", "Can edit food type"),
            ("can_delete_foodtype", "Can delete food type"),
        ]

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, verbose_name="Type of Food")
    name = models.CharField(max_length=100, verbose_name="Food Name")
    ingredients = models.TextField(verbose_name="Ingredients")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    view_count = models.PositiveIntegerField(default=0, verbose_name="View Count")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Created By", related_name="foods", default=1)  # Provide a default user ID
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name_plural = "Foods"
        permissions = [
            ("can_add_food", "Can add food"),
            ("can_edit_food", "Can edit food"),
            ("can_delete_food", "Can delete food"),
        ]

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'food')   

    def __str__(self):
        return f"{self.user.username} likes {self.food.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Comment Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Comment by {self.user.username} on {self.food.name}"

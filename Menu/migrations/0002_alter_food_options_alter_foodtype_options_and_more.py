# Generated by Django 5.1.2 on 2024-10-24 15:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'permissions': [('can_add_food', 'Can add food'), ('can_edit_food', 'Can edit food'), ('can_delete_food', 'Can delete food')], 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterModelOptions(
            name='foodtype',
            options={'permissions': [('can_add_foodtype', 'Can add food type'), ('can_edit_foodtype', 'Can edit food type'), ('can_delete_foodtype', 'Can delete food type')], 'verbose_name_plural': 'Food Types'},
        ),
        migrations.AddField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
        ),
        migrations.AddField(
            model_name='food',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='food',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]

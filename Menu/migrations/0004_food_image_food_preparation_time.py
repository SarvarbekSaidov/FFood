# Generated by Django 5.1.2 on 2024-10-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='food_images/', verbose_name='Food Image'),
        ),
        migrations.AddField(
            model_name='food',
            name='preparation_time',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Preparation Time (minutes)'),
        ),
    ]

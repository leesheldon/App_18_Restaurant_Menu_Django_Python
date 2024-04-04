# Generated by Django 5.0.4 on 2024-04-04 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=1000, unique=True)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('meal_type', models.CharField(choices=[('starters', 'Starters'), ('salads', 'Salads'), ('main_dishes', 'Main Dishes'), ('desserts', 'Desserts')], max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

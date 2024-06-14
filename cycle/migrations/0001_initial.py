# Generated by Django 5.0.6 on 2024-06-12 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasktodo', '0006_task_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Сlassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('slug', models.SlugField(max_length=90, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created', 'name'],
                'indexes': [models.Index(fields=['created'], name='cycle_сlass_created_9e8c5a_idx'), models.Index(fields=['name'], name='cycle_сlass_name_1da979_idx')],
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ManyToManyField(related_name='cycles', to='tasktodo.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cycles', to=settings.AUTH_USER_MODEL)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classifications', to='cycle.сlassification')),
            ],
            options={
                'ordering': ['classification'],
                'indexes': [models.Index(fields=['classification'], name='cycle_cycle_classif_1a6349_idx')],
            },
        ),
    ]
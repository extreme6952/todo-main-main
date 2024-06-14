from tasktodo.models import Task

from decimal import Decimal

from django.conf import settings

from django.db import models

from django.contrib.auth.models import User



class Сlassification(models.Model):

    name = models.CharField(max_length=75,
                            unique=True,)
    
    slug = models.SlugField(max_length=90,
                            unique=True)
    
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)
    
    class Meta:

        ordering = ['created','name']

        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['name'])
        ]

    def __str__(self) -> str:
        return f"Имя классификации {self.name}"



class Cycle(models.Model):

    classification = models.ForeignKey(Сlassification,
                                       on_delete=models.CASCADE,
                                       related_name='classifications')
    
    task = models.ManyToManyField(Task,
                                related_name='cycles')
    
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='cycles')
    
    class Meta:

        ordering = ['classification']

        indexes = [
            models.Index(fields=['classification'])
        ]

    def __str__(self):

        f"Цикл задач пользователя {self.user.username} в классификации {self.cl}"
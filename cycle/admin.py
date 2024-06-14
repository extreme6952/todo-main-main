from django.contrib import admin

from .models import *


@admin.register(Сlassification)
class AdminModelClassification(admin.ModelAdmin):

    list_display = ['name','slug']

    list_filter = ['created','updated']

    prepopulated_fields = {'slug':('name',)}


@admin.register(Cycle)
class AdminModelCycle(admin.ModelAdmin):

    list_display = ['classification','user','get_tasks']



    def get_tasks(self, obj):
        return ', '.join([str(task) for task in obj.task.all()])


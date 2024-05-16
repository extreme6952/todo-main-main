from django.contrib import admin

from .models import *


@admin.register(Actions)
class ActionAdmin(admin.ModelAdmin):

    list_display = ['user','verb','created']

    list_filter = ['created']

    search_fields = ['verb']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['user','created','active']

    list_filter = ['created','active']

    
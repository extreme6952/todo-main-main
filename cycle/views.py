from django.shortcuts import render,get_object_or_404,redirect

from .forms import *

from tasktodo.models import Task

from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required



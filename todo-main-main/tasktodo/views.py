from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import *

from .models import *

from django.shortcuts import redirect

from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.models import User

from actions.models import *


@login_required
def task_list(request):

    task = Task.objects.all()

    if request.method=='POST':

        form = NewTaskForm(data=request.POST,
                           files=request.FILES)
        
        if form.is_valid():

            cd = form.cleaned_data

            new_task = form.save(commit=False)

            new_task.user = request.user

            new_task.save()

            messages.success(request,
                             'Задача успешно добавлена')

            return redirect(new_task.get_absolute_url())
        
        else:

            messages.error(request,
                           'При заполнении данных произошла ошибка')
            

    else:

        form = NewTaskForm(files=request.FILES,
                           data=request.GET)
        

    return render(request,
                  'task/task_list.html',
                  {'task':task,
                   'form':form})

@login_required
def task_detail(request,task_id,slug):

    task = get_object_or_404(Task,
                             id=task_id,
                             slug=slug)
    
    form = CommentForm()
    
    comments = task.comments.filter(active=True)
    
    
    
    

    
    return render(request,
                  'task/task_detail.html',
                  {'task_detail':task,
                   'comments':comments,
                   'form':form})

def update_task(request,slug,task_id):

    task = get_object_or_404(Task,
                             slug=slug,
                             id=task_id)
    
    task.is_complete = not task.is_complete

    task.save()

    return redirect('index')


def delete_task(request,id,slug):

    task = get_object_or_404(Task,slug=slug,
                             id=id)
    task.delete()



def delete_task(request,task_id,slug):

    task = get_object_or_404(Task,slug=slug,
                             id=task_id)
    task.delete()

    

    return redirect('index')





# comment task in contenttype
@login_required
@require_POST
def add_comment(request,slug,id):   

    task = get_object_or_404(Task,
                             slug=slug,
                             id=id)
    
    comment = None

    if request.method == 'POST':

        form = CommentForm(data=request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.user = request.user

            comment.task = task

            comment.save()

            messages.success(request,
                             'Ваш комментарий был успешно добавлен')
            
            return redirect(task.get_absolute_url())

    else:

        form = CommentForm()

    return render(request,
                  'task/comment.html',
                  {'task':task,
                   'comment':comment,
                   'form':form})


             






@login_required
def like_post(request, id, slug):
    task = get_object_or_404(Task, id=id, slug=slug)

    try:
        if request.user in task.users_like.all():
            # Пользователь уже поставил лайк этому посту, удаляем его
            task.users_like.remove(request.user)
            return redirect(task.get_absolute_url())
        else:
            # Пользователь ещё не поставил лайк, добавляем его
            task.users_like.add(request.user)
            return redirect(task.get_absolute_url())
    except Task.DoesNotExist:
        # Если объект Task не найден, перенаправляем пользователя на страницу 404
        return redirect('404')
    

def user_registration(request):

    if request.method=='POST':

        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()

            Profile.objects.create(user=new_user)

            messages.success(request,'Спасибо,что зарегестрировались на нашем сайте')

            return redirect('index')
        
        else:

            messages.error(request,
                           'При заполнении данных произошла ошибка')
            
    else:

        user_form = UserRegistrationForm()

    return render(request,
                  'registration/user_registration.html',
                  {'user_form':user_form})



@login_required
def user_list(request):

    users = User.objects.filter(is_active=True)

    return render(request,
                  'task/user_list.html',
                  {'users':users})




@login_required
def user_detail(request,username):

    user_detail = get_object_or_404(User,
                                    is_active=True,
                                    username=username)
    
    return render(request,
                  'task/user_detail.html',
                  {'user_detail':user_detail})
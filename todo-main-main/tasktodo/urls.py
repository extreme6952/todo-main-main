from django.urls import include, path



from . import  views


urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    
    path('',views.task_list,name='index'),

    path('<int:task_id>/<slug:slug>/', views.task_detail,name='task_detail'),

    path('update/<int:task_id>/<slug:slug>',views.update_task,name='update'),

    path('delete/<int:task_id>/<slug:slug>/',views.delete_task,name='delete_suka'),

    path('<int:id>/<slug:slug>/like/',views.like_post,name='task_like'),

    path('comment/',views.add_comment,name='commetd'),

    path('registration/',views.user_registration,name='user_registration'),

    path('user-list/',views.user_list,name='user_list'),

    path('user-detail/<username>/',views.user_detail,name='user_detail'),

    path('add-comment/<slug:slug>/<int:id>/',views.add_comment,name='commetd')
    
    
]

from django.shortcuts import render

# Create your views here.

def chat_view(request):

    return render(request,
                  'chatapp/index.html')


def chat_room(request,room_name):

    return render(request,
                  'chatapp/room.html',
                  {'room_name':room_name})
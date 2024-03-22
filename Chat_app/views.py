from django.shortcuts import render, redirect
from .models import Room, Message


def CreateRoom(request):
    if request.method == "POST":
        username = request.POST['username']
        room = request.POST['room']

        try: # This will create a new room if room name doesn't exist
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)
        except Room.DoesNotExist: # This will redirect to the room if room name it exist
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room, username=username)
    return render(request, 'index.html')


# This view will take in the room_name and the username of the user before being able to message.
def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)

    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
    }
    return render(request, '_message.html', context)

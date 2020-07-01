from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Q # for "or"

from chat_room.models import *
from chat_room.serializer import RoomSerializers
from chat_room.serializer import UserSerializers
from chat_room.serializer import ChatSerializers
from chat_room.serializer import ChatPostSerializers
from django.contrib.auth.models import User


class RoomView(APIView):
  # Комната чата
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    rooms = Room.objects.filter(Q(invited = request.user) | Q(creater = request.user) )
    serializer = RoomSerializers(rooms, many = True)
    return Response({"data": serializer.data})

  def post(self, request):
      # room = request.GET.get("room")
      Room.objects.create(creater = request.user)
      return Response(status=201)
      
class ChatView(APIView):
  # Комната чата
  permission_classes = [permissions.IsAuthenticated]
  #permission_classes = [permissions.AllowAny]
  def get(self, request):
    room = request.GET.get("room")
    chat = Chat.objects.filter(room = room)
    serializer = ChatSerializers(chat, many = True)
    return Response({"data": serializer.data})


  def post(self, request):
    # room = request.GET.get("room")
    dialog = ChatPostSerializers(data=request.data)
    if dialog.is_valid():
      dialog.save(user = request.user)
      return Response({"status":"Add"})
    else:
      return Response({"status":"Error"})

class AddUsersRoom(APIView):
  #add users in room chat
  def get(self, request):
    users =User.objects.all()
    serializer = UserSerializers(users, many = True)
    return Response(serializer.data)

  def post(self, request):
    room = request.data.get("room")
    user = request.data.get("user")
    try:
      room = Room.objects.get(id = room)
      room.invited.add(user)
      room.save()
      return Response(status=201)
    except:
      return Response(status=400)

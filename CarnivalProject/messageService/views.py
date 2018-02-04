from django.shortcuts import render
from .models import Chat,Message
from . import models
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def createChat(nickname1, nickname2):
    chat = Chat.objects.create(nickname1=nickname1, nickname2=nickname2,lastMessage="")
    chat.save()
    return chat

def createMessage(sendNickname, fromNickname, msg):
    message = Message.objects.create(from_nickname=fromNickname, to_nickname=sendNickname, msg=msg)
    message.save()
    return message


# retreive all users registered to site
def getAllUsers(request):
    allUsers = models.User.objects
    return render(request, 'messageService/allUsers.html', {'all_users': allUsers})


def userSelected(selectedUser):

  chat_exists = Chat.objects.filter(nickname1=)
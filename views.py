from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot

def index(request):
  return render(request,'blog/index.html')

def specific(request):
  return HttpResponse("This is the specific url")

def getResponse(request):
  userMessage = request.GET.get('userMessage')
  return HttpResponse(userMessage)
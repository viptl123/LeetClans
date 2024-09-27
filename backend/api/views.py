from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def get_user(request):
    if request.method == "POST":
        print(request.data)
        return Response(UserSerializer({'name': 'kowalski', 'username': "hello", "trophies": 30}).data)
    elif request.method == "GET":
        print("fnioe")
        return Response(UserSerializer({'name': 'Pedro', 'username': "hello", "trophies": 30}).data)
    

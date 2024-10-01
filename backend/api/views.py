from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer
import boto3
from dotenv import load_dotenv
import os


load_dotenv()
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

@api_view(['GET', 'POST'])


def get_user(request):
    print(aws_access_key_id)
    print(aws_secret_access_key)
    s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)
    # List all buckets

    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')




    if request.method == "POST":
        print(request.data)
        return Response(UserSerializer({'name': 'kowalski', 'username': "hello", "trophies": 30}).data)
    elif request.method == "GET":
        print("fnioe")
        return Response(UserSerializer({'name': 'Pedro', 'username': "hello", "trophies": 30}).data)
    


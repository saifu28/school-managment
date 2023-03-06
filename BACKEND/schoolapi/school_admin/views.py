from django.shortcuts import render
from .models import Admin
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(['POST'])
def admin_home(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        check = Admin.objects.get(username = username,password = password)
        status = True
    except:
        status = False

    return JsonResponse({'status':status})




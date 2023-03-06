from django.http import JsonResponse
from django.shortcuts import render
from .models import Teacher
from rest_framework.decorators import api_view
from .serializers import Teacherserializer

# Create your views here.
api_view(['POST'])
def add_teacher(request):
    try:
        teacher_data = request.data
        print(teacher_data,'ddddddddddd')
        email_ex = Teacher.objects.filter(email=teacher_data['email']).exists()
        if not email_ex:
            s_data = Teacherserializer(data = teacher_data)
            if s_data.is_valid():
                s_data.save()
                msg = 'Teacher added'
            else:
                msg = 'From error'

        else:
            msg = 'E-mail already exist..'
    
    except Exception as d:
        print(d)
        msg = 'Somthing went wrong !!!'

    return JsonResponse({'msg':msg})
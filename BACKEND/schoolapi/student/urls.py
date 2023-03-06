from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('student_home',views.student_home)
]
from django.urls import path
from . import views

app_name = 'school_admin'

urlpatterns = [
    path('admin_home',views.admin_home)
]
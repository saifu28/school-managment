from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher_tb'
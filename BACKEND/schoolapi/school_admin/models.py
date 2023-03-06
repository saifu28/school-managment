from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class meta:
        db_table = 'admin_tb'

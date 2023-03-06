from rest_framework import serializers
from .models import Teacher

class Teacherserializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
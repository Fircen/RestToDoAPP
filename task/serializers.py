
from dataclasses import field
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):

    class Meta:
        model = Task
        field = '__all__'
from django.shortcuts import render
from rest_framework import generics
from .models import Task
from task.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated 
# Create your views here.
class TaskView(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def perorm_create(self,serializer):
        return serializer.save(owner = self.request.user)
    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)
from django.shortcuts import render
from rest_framework import generics
from .serializers import LoginSerializer, UserSerializer
from django.http import HttpResponse, JsonResponse
# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data = user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data = user)
        serializer.is_valid(raise_exception = True)
        return JsonResponse(serializer.data, status=200)


from django.shortcuts import render
from django.http import HttpResponse
from .serializers import RegisterationSerializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.values()
        serializer = RegisterationSerializers(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    """  Creating user  """
    def post(self, request):
        serializer = RegisterationSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response ({"messages" : "berhasil di kirim"}, status=status.HTTP_201_CREATED)

        return Response({'messages' : 'terjadi sebuah error saat register'}, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

from django.shortcuts import render

from django.http import response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Users
from . serializers import Usersserializer

class Userslist(APIView):
    def get(self,request):
        Users1 = Users.objects.all()
        serializer=Usersserializer(Users1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
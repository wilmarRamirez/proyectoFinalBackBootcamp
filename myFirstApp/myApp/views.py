from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from django.http import Http404

class Exclusive_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Exclusive.objects.all()
        serializer = ExclusiveSerializers(post, many=True)

        return Response(serializer.data)

    def Exclusive(self, request, format=None):
        serializer = ExclusiveSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Best_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Best.objects.all()
        serializer = BestSerializers(post, many=True)

        return Response(serializer.data)

    def Best(self, request, format=None):
        serializer = BestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LatestBlog_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = LatestBlog.objects.all()
        serializer = LatestBlogSerializers(post, many=True)

        return Response(serializer.data)

    def LatestBlog(self, request, format=None):
        serializer = LatestBlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


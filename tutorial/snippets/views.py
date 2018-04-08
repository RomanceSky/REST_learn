# -*- coding: utf-8 -*-
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from snippets.serializer import UserSerializer
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.renderers import JSONRenderer
#: 为视图添加需要的权限
from rest_framework import permissions


#: 使用基于视图的一般类——generic class
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


#: 使用基于视图的一般类ListAPIView和RetrieveAPIView
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

def apitestView(request):
   # data = request.POST['data']
    return JsonResponse({'data':'data'})

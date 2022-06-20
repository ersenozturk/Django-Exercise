from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
import rest_framework
from rest_framework import serializers


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import action

# pagination classes:
from .pagination import MyCursorPagination, MyLimitOffsetPagination, SmallPageNumberPagination, LargePageNumberPagination

# filter backend
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

# auth and permission

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
)
from .permissions import IsAdminOrReadOnly

# Create your views here.


def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )


class TodoMVS(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # pagination_class = LargePageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['task', "priority"]
    search_fields = ['task']
    ordering_fields = ['task', "createdDate", "id"]

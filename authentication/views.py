from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserDetailsSerializer
from .permissions import IsFastChecker, IsSimpleUser
from rest_framework import filters
from rest_framework import filters

# create user
# class UserCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny,)

# api

class UserDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(request.user.email)

# Create your views here.
class AllUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', "last_name", 'email']
#     search_fields = ['username', 'email', 'profile__profession']
# search_fields = ['data__breed', 'data__owner__other_pets__0__name']

# Create your views here.
# class AllNotFCUsersView(generics.ListAPIView):
#     queryset = CustomUser.objects.all().filter(is_fc=False)
#     serializer_class = CustomUserDetailsSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['first_name', "last_name", 'email']
#     search_fields = ['username', 'email', 'profile__profession']
# search_fields = ['data__breed', 'data__owner__other_pets__0__name']



class HelloAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = {
            'message' : 'Hello Django REST API'
        }
        return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def hello_drf(request):
    data = {
            'message' : 'Hello Django REST API. @api_view'
        }
    return Response(data)


################ role-based
class HelloRoleAPI(APIView):
    permission_classes = [IsFastChecker]
    def get(self, request):
        data = {
            'message' : 'Hello Django REST API'
        }
        return Response(data)


@api_view(["GET"])
@permission_classes([IsSimpleUser])
def hello_role_drf(request):
    data = {
            'message' : 'Hello Django REST API. @api_view'
        }
    return Response(data)
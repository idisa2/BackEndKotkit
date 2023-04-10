from django.shortcuts import render
from django.core.files import File
from django.db.models import Q
from rest_framework import viewsets, generics, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, \
    IsAdminUser, DjangoModelPermissions, AllowAny
import json

# Create your views here.
from pal.models import KitKot
from pal.serializers import KitKotSerializer


class KitKotListCreate(generics.ListCreateAPIView):
    # queryset = models.Category.objects.all()
    serializer_class = KitKotSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['title', "tags", "description", ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        # reveals = Category.objects.filter(created_by=request.user.id)
        objs = KitKot.objects.filter()
        return objs


class KitKotDetail(generics.RetrieveUpdateDestroyAPIView, ):
    permission_classes = [IsAuthenticated]
    queryset = KitKot.objects.all()
    serializer_class = KitKotSerializer


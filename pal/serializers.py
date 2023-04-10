from django.shortcuts import render
from rest_framework import serializers, status

from authentication.serializers import CustomUserDetailsSerializer

# Create your views here.
from pal.models import KitKot


class KitKotSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = KitKot
        fields = ['id', 'title', "description", "tags",  'image', "video", "created_at",  "created_by",
                  ]

    def get_created_by(self, o):
        if o.created_by:
            obj = CustomUserDetailsSerializer(o.created_by).data
            return obj
        else:
            return None

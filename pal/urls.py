from django.urls import path, re_path

from pal import consumers
from pal.views import KitKotListCreate, KitKotDetail

app_name = 'pal'

urlpatterns = [

    path('videos', KitKotListCreate.as_view(), name='videos'),
    path('videos/<int:pk>', KitKotDetail.as_view(), name='video'),

]

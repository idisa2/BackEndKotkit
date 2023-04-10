from django.urls import include, path , re_path as url
# from django.conf.urls import url
from . import views
from .views import UserDetailsView, AllUsersView
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# router = routers.DefaultRouter()
# router.register('users', views.UserViewSet)
# router.register('me', views.UserDetailsView)

urlpatterns = [        
    # url(r'api/users/create', views.UserCreateAPIView.as_view(), name='create'),

    path('me/', UserDetailsView.as_view(), name='me'),
    path('all/', AllUsersView.as_view(), name='all_users'),
    # path('allnotfc/', AllNotFCUsersView.as_view(), name='all_not_fc_users'),


    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

    path('api/hello', views.HelloAPI.as_view(), name = 'hello_api'),
    path('api/hello2', views.hello_drf, name='hello_api2'),

    path('api/hellorole', views.HelloRoleAPI.as_view(), name = 'hello_role_api'),
    path('api/hellorole2', views.hello_role_drf, name='hello_role_api2'),

]
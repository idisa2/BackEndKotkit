from django.contrib import admin
from django.urls import path, include, re_path as url
# from django.conf.urls import url
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView

from pal import consumers

urlpatterns = [
    # path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), ),

    #  activate the email account after the user clicks on the link received in the email
    path('auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), ),
    # Sign-up with email verification
    path('auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # Needs to be defined before the registration path
    # password reset
    path('rest-auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('admin/', admin.site.urls, ),
    url('auth/', include('dj_rest_auth.urls')),
    # path('', include('blog.urls')),
    path('', include('authentication.urls')),
    # registration
    url('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/reveal/', include('reveal.urls')),
    # path('api/speaker/', include('speakerrecognition.urls')),
    path('api/kitkot/', include('pal.urls')),
    path('tinymce/', include('tinymce.urls')),

]

# websocket_urlpatterns = [
#     re_path(r'ws/chat/room/$', consumers.RoomConsumer.as_asgi()),
# ]

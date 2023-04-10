# serializers.py in the users Django app
from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from authentication.models import GENDER_SELECTION, CustomUser
from dj_rest_auth.serializers import PasswordResetSerializer
from django.contrib.auth.tokens import default_token_generator

class CustomRegisterSerializer(RegisterSerializer): 
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    phone_number = serializers.CharField(max_length=30)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.phone_number = self.data.get('phone_number')
        user.whatsapp_number = self.data.get('whatsapp_number')
        # user.fcm_token = self.data.get('fcm_token', None)
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            "username",
            'phone_number',
            'gender',
            'first_name',
            'last_name',
            'groups',
            'is_active',
            'whatsapp_number',
            'balance',
            # 'is_fc',
            # "fc_id",
            # 'fcm_token'
        )
        read_only_fields = ('id', 'email', 'phone_number',)


class CustomPasswordResetSerializer(PasswordResetSerializer):

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        print("***************************")
        print(self.initial_data)
        print("***************************")
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value


    def save(self):
        print("hello world")
        request = self.context.get('request')
        # token = default_token_generator.make_token(request.user)
        # print(request.query_params)
        # print(request.user.email)
        # print(request.user.username)
        # print(request.user.pk)
        # print(request.user.gender)
        print(request.user.gender)
        # print(token)
        print("---------------")
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': 'example@yourdomain.com',
            'request': request,
            # here I have set my desired template to be used
            # don't forget to add your templates directory in settings to be found
            # 'email_template_name': 'password_reset_email.html'
        }
        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
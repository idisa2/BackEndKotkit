# models.py in the users Django app
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    phone_number = models.CharField(max_length=30)
    whatsapp_number = models.CharField(max_length=30, blank=True, null=True)
    actif = models.BooleanField(default=True, verbose_name="Mobile App Access")
    balance = models.FloatField(null=False, blank=False, default=0)

    # fcm_token = models.TextField(blank=True, null=True)

    # nationality = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, related_name='user_country',  verbose_name="Country")
    # is_fc = models.BooleanField(default=False, verbose_name="Is FC")
    # fc_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.email)

from django.db import models

# Create your models here.
from authentication.models import CustomUser


class KitKot(models.Model):
    class Meta:
        verbose_name = 'KitKot'
        verbose_name_plural = 'KitKots'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=240, default='desciption')
    tags = models.CharField(max_length=240, default='desciption')
    image = models.ImageField(upload_to="kitkot/uploads/images/", blank=True, null=True)
    video = models.FileField(upload_to="kitkot/uploads/video/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    created_by = models.ForeignKey(CustomUser, blank=False,   null=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
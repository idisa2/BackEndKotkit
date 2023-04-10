from django.contrib import admin

# Register your models here.
from authentication.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):

    readonly_fields = ("id",  "username", "email", "password")
    list_filter = ("id", "actif")
    search_fields = ("last_name__startswith", "first_name__startswith", "phone_number__startswith")
    list_display = ("id", "first_name", "last_name",  "email", "phone_number", "actif",)
    ordering = ('id', 'actif')
    # date_hierarchy = ('created_at')
    # raw_id_fields = ('id',)

admin.site.register(CustomUser, CustomUserAdmin)
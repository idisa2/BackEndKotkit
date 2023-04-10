from django.contrib import admin

# Register your models here.
from pal.models import KitKot


@admin.register(KitKot)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_by"  )
    list_filter = ("id",)
    # search_fields = ("name__startswith",  )
    ordering = ['id']
    readonly_fields = ('id', )


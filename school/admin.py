from django.contrib import admin

# Register your models here.
from school.models import Country, Site, Language, Technology, Course, TrainerProfile, StudentProfile, Parcours


class CountryAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "name", "flag", "iso", "enabled", )
    list_filter = ("created_by", "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    raw_id_fields = ('created_by',)


admin.site.register(Country, CountryAdmin)


class SiteAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "name", "enabled", )
    list_filter = ("created_by", "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    raw_id_fields = ('created_by',)


admin.site.register(Site, SiteAdmin)


class LanguageAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "name", "enabled", )
    list_filter = ("created_by", "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    raw_id_fields = ('created_by',)


admin.site.register(Language, LanguageAdmin)


class TechnologyAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "name", "enabled", )
    list_filter = ("created_by", "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    raw_id_fields = ('created_by',)


admin.site.register(Technology, TechnologyAdmin)


class CourseAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "name", "enabled", "fee", "technology" )
    list_filter = ("created_by", "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    raw_id_fields = ('created_by',)


admin.site.register(Course, CourseAdmin)


class TrainerProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "nationality", "enabled", "account")
    list_filter = ( "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    # raw_id_fields = ('created_by',)


admin.site.register(TrainerProfile, TrainerProfileAdmin)


class StudentProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('id', "created_at")
    list_display = ("id", "nationality", "enabled", "account")
    list_filter = ("enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', 'created_at')
    date_hierarchy = ('created_at')
    # raw_id_fields = ('created_by',)


admin.site.register(StudentProfile, StudentProfileAdmin)


class ParcoursAdmin(admin.ModelAdmin):

    readonly_fields = ('id', )
    list_display = ("id", "name", "enabled", "fee")
    list_filter = ("created_by", "enabled", )
    # search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
    ordering = ('id', )
    # date_hierarchy = ('created_at')
    raw_id_fields = ('created_by',)


admin.site.register(Parcours, ParcoursAdmin)


# class PooiAdmin(admin.ModelAdmin):
#
#     readonly_fields = ('id', "created_at")
#     list_display = ("id", "first_name", "last_name", "voice_validated", "name", "email", "mobile_phone", "website", "wikipedia", "imdb", "twitter", "linkedin", "facebook", "instagram", "youtube")
#     list_filter = ("created_by", "first_name", "last_name", "name", "email", "mobile_phone", "voice_validated")
#     search_fields = ("last_name__startswith", "last_name__startswith", "name__startswith", "email__startswith", "mobile_phone__startswith",)
#     ordering = ('id', 'created_at')
#     date_hierarchy = ('created_at')
#     raw_id_fields = ('created_by',)
#     inlines = [
#         VoiceSampleInline, ImageSampleInline
#     ]
#
#
# admin.site.register(Pooi, PooiAdmin)

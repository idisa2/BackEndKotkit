
from rest_framework import serializers, status

from authentication.serializers import CustomUserDetailsSerializer
from school.models import Country, Site, Language, Technology, Course, Parcours, TrainerProfile, StudentProfile


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", 'name', 'flag', 'iso', 'created_at']


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ["id", 'name', 'addresse', 'lat', 'long', 'country', 'created_at']

    def get_country(self, obj):
        if obj.country:
            return CountrySerializer(obj.country).data
        else:
            return None


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", 'name', 'logo', 'created_at']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", 'name', 'logo', 'language', 'created_at']

    def get_language(self, obj):
        if obj.language:
            return LanguageSerializer(obj.language).data
        else:
            return None


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", 'name', 'logo', 'technology', 'video', 'duration', 'fee', 'short_description', 'long_description', 'requirements', 'job_opportunities', 'created_at']

    def get_technology(self, obj):
        if obj.technology:
            return TechnologySerializer(obj.technology).data
        else:
            return None


class TrainerProfileSerializer(serializers.ModelSerializer):
    curriculum = serializers.SerializerMethodField()
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = TrainerProfile
        fields = ["id", 'address', 'nationality', 'curriculum',  'technologies', 'niveau', 'comments', 'twitter', 'linkedin', 'facebook', 'youtube', 'github', 'website', 'account', 'created_at']

    def get_nationality(self, obj):
        if obj.nationality:
            return CountrySerializer(obj.nationality).data
        else:
            return None

    def get_curriculum(self, obj):
        if obj.curriculum:
            return CourseSerializer(obj.curriculum, many=True).data
        else:
            return []

    def get_technologies(self, obj):
        if obj.technologies:
            return TechnologySerializer(obj.v, many=True).data
        else:
            return []

    def get_account(self, obj):
        return CustomUserDetailsSerializer(obj.account).data


class StudentProfileSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = ["id", 'address', 'nationality', 'technologies', 'niveau', 'comments', 'twitter', 'linkedin', 'facebook', 'youtube', 'github', 'website', 'account', 'created_at']

    def get_nationality(self, obj):
        if obj.nationality:
            return CountrySerializer(obj.nationality).data
        else:
            return None

    def get_technologies(self, obj):
        if obj.technologies:
            return TechnologySerializer(obj.v, many=True).data
        else:
            return []

    def get_account(self, obj):
        return CustomUserDetailsSerializer(obj.account).data


class ParcoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcours
        fields = ["id", 'name', 'logo', 'video', 'duration', 'internship_duration', 'fee', 'short_description', 'long_description', 'requirements', 'job_opportunities', 'curriculum', 'created_at']

    def get_technology(self, obj):
        if obj.technology:
            return TechnologySerializer(obj.technology).data
        else:
            return None

    def get_curriculum(self, obj):
        if obj.curriculum:
            return CourseSerializer(obj.curriculum, many=True).data
        else:
            return []

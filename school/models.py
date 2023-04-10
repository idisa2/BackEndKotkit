from django.db import models

# Create your models here.
from authentication.models import CustomUser

EDUCATION_QUALIFICATION = [
    ('Secondaire', 'Secondaire'),
    ('BAC', 'BAC'),
    ('BAC+2', 'BAC+2'),
    ('Licence', 'Licence'),
    ('Maitrise', 'Maitrise'),
    ('Master', 'Master'),
    ('Doctorat', 'Doctorat'),
]

PROFESSIONNNAL_STATUS = [
    ('Sans emploie', 'Secondaire'),
    ('Freelance', 'BAC'),
    ('En entreprise', 'BAC+2'),
    ('Licence', 'Licence'),
    ('Maitrise', 'Maitrise'),
    ('Master', 'Master'),
    ('Doctorat', 'Doctorat'),
]

TRAINING_FORMATS = [
    ('Présentiel', 'Présentiel'),
    ('En Ligne', 'En Ligne'),
    ('Hybride', 'Hybride'),
]

from django.db import models
from tinymce.models import HTMLField

class Country(models.Model):
    class Meta:
        verbose_name = 'County'
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='country_flags', null=True, blank=True, )
    flag_emoji = models.CharField(max_length=100, default='🇧🇯')
    iso = models.CharField(max_length=100, unique=True)
    enabled = models.BooleanField(default=True, verbose_name="Show on app")
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Site(models.Model):
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    name = models.CharField(max_length=100)
    addresse = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    long = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    enabled = models.BooleanField(default=True, verbose_name="Show on app")
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='site_country',  verbose_name="Site")
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Language(models.Model):
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos',)
    enabled = models.BooleanField(default=True, verbose_name="Show on app")
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Technology(models.Model):
    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='technologies',)
    enabled = models.BooleanField(default=True, verbose_name="Show on app")
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    language = models.ForeignKey(Language, related_name='technology_language',blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Course(models.Model):
    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'

    enabled = models.BooleanField(default=True, verbose_name="Show on app")
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='courses',)
    video = models.FileField(upload_to='courses', blank=True, null=True)
    duration = models.IntegerField()
    # internship_duration = models.IntegerField(max_length=5)
    fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    short_description = models.TextField(max_length=500, blank=True, null=True)
    long_description = HTMLField(),
    requirements = models.TextField(max_length=500, blank=True, null=True)
    job_opportunities = models.TextField(max_length=500, blank=True, null=True)
    technology = models.ForeignKey(Technology, related_name='technology_courses', on_delete=models.CASCADE, verbose_name="training")
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )

    def __str__(self):
        return self.name


class TrainerProfile(models.Model):
    class Meta:
        verbose_name = 'TrainerProfile'
        verbose_name_plural = 'TrainerProfiles'

    enabled = models.BooleanField(default=True, verbose_name="Active profile")
    address = models.CharField(max_length=250, blank=True, null=True, )
    nationality = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, related_name='country_trainers',  verbose_name="Country")
    curriculum = models.ManyToManyField(Course, related_name='courses_trainers', verbose_name="Curriculum")
    technologies = models.ManyToManyField(Technology, related_name='profile_technologies', verbose_name="Technologies")
    niveau = models.CharField(max_length=50, choices=EDUCATION_QUALIFICATION)
    comments = models.TextField(max_length=1000, blank=True, null=True)
    twitter = models.CharField(blank=True, null=True, max_length=100)
    linkedin = models.CharField(blank=True, null=True, max_length=100)
    facebook = models.CharField(blank=True, null=True, max_length=100)
    youtube = models.CharField(blank=True, null=True, max_length=100)
    github = models.CharField(blank=True, null=True, max_length=100)
    website = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) +" - "+ self.account.name

    def country_name(self):
        if self.nationality:
            return self.nationality.name
        return "-"


class StudentProfile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    enabled = models.BooleanField(default=True, verbose_name="Active profile")
    address = models.CharField(max_length=250, blank=True, null=True, )
    nationality = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, related_name='country_students',  verbose_name="Country")
    technologies = models.ManyToManyField(Technology, related_name='technology_students', verbose_name="Technologies")
    niveau = models.CharField(max_length=50, choices=EDUCATION_QUALIFICATION)
    comments = models.TextField(max_length=1000, blank=True, null=True)
    twitter = models.CharField(blank=True, null=True, max_length=100)
    linkedin = models.CharField(blank=True, null=True, max_length=100)
    facebook = models.CharField(blank=True, null=True, max_length=100)
    youtube = models.CharField(blank=True, null=True, max_length=100)
    github = models.CharField(blank=True, null=True, max_length=100)
    website = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) +" - "+ self.account.name

    def country_name(self):
        if self.nationality:
            return self.nationality.name
        return "-"


class Parcours(models.Model):
    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'

    enabled = models.BooleanField(default=True, verbose_name="Show on app")
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='trainings',)
    video = models.FileField(upload_to='trainings', blank=True, null=True)
    duration = models.IntegerField()
    internship_duration = models.IntegerField()
    fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    short_description = models.TextField(max_length=500, blank=True, null=True)
    long_description = HTMLField(),
    requirements = models.TextField(max_length=500, blank=True, null=True)
    job_opportunities = models.TextField(max_length=500, blank=True, null=True)
    curriculum = models.ManyToManyField(Course, related_name='courses_parccours', verbose_name="Curriculum")
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, )

    def __str__(self):
        return str(self.id) + self.account.name


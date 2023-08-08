from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    photo = models.TextField()
    user_type = models.CharField(max_length=20)  # Possible values: 'Provider', 'Customer', 'Admin'

class JobListing(models.Model):
    job_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    posted_date = models.DateField()

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    job_seeker = models.ForeignKey('JobSeeker', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    job_seeker = models.ForeignKey('JobSeeker', on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True)
    graduation_date = models.DateField()

class JobSeeker(models.Model):
    job_seeker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    resume = models.TextField()
    skills = models.TextField()

class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=20)  # Possible values: 'Applied', 'Under Review', 'Accepted', 'Rejected'

class SearchPreferences(models.Model):
    preference_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50)

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    sent_date = models.DateTimeField()

class UserCredentials(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=255)

class CustomUser(AbstractUser):

    REQUIRED_FIELDS = ['email']
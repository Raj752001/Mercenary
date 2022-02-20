from operator import mod
from pyexpat import model
from re import S
from typing import Type
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

from .models import Skill, Profession, Members

# Create your models here.
class Mercenary(models.Model):
    STATUS = (
        ('OP', 'Open for Missions'),
        ('WM', 'Working on Missions'),
        ('CL', 'Closed'),
    )
    RANK = (
        ('F', 'Novice'),
        ('E', 'Novice'),
        ('D', 'Closed'),
        ('C', 'Closed'),
        ('B', 'Closed'),
        ('A', 'Closed'),
        ('S', 'Closed'),
        ('S+', 'Hard Core'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS)
    about = models.TextField(max_length=500, blank=True, null=True)
    profession = models.ManyToManyField(Profession)
    highest_education = models.CharField(max_length=50, blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)
    skills = models.ManyToManyField(Skill) # many to many
    contact_number = models.IntegerField(max_length=10, blank=True, null=True)
    linkedin_link = models.URLField(max_length=100, blank=True, null=True)
    github_link = models.URLField(max_length=100, blank=True, null=True)
    rank = models.CharField(max_length=2, choices=RANK)


class Skill(models.Model):
    name = models.CharField(primary_key=True, max_length=20)


class Profession(models.Model):
    name = models.CharField(primary_key=True, max_length=20)


class Tags(models.Model):
    tag = models.CharField(primary_key=True, max_length=20)


class Mission(models.Model):
    STATUS = (
        ('OP', 'Ongoing'),
        ('IN', 'Incubating'),
        ('CP', 'Completed'),
    )
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=100, blank=True, null=True)
    repo_link = models.URLField(max_length=100, blank=True, null=True)
    status = models.CharField(choices=STATUS, blank=True, null=True)
    recruiting = models.BooleanField(default=False)
    # rank = models.CharField() #(Duration, members, technologies, )
    technologies = models.ManyToManyField(Skill)
    tags = models.ManyToManyField(Tags)
    op = models.ForeignKey(Mercenary, related_name="missions")


class Members(models.Model):
    mission = models.ForeignKey(Mission, primary_key=True)
    mercenary = models.ForeignKey(Mercenary, related_name="commissions", primary_key=True)
    role = models.CharField(max_length=100, blank=True, null=True)


class Requests(models.Model):
    TYPE = (
        ('A', 'Apply'),
        ('R', 'Request'),
    )
    mission = models.ForeignKey(Mission, related_name="requests", primary_key=True)
    mercenary = models.ForeignKey(Mercenary, related_name="applies", primary_key=True)
    type = models.CharField(max_length=1, choices=TYPE)
    message = models.TextField(max_length=200, blank=True, null=True)

class Images(models.Model):
    id = models.UUIDField(primary_key=True)
    image = models.ImageField()

class Feedback(models.Model):
    id = models.UUIDField(primary_key=True)
    subject = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.ManyToManyField(Images)

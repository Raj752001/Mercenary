from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField()
    name = models.CharField()
    status = models.CharField() 
    profession = models.CharField()
    highest_education = models.CharField()
    college = models.CharField()
    # skills = models.ForeignKey() # 1 to many
    about = models.TextField()
    contact_number = models.IntegerField()
    linkedin_link = models.URLField()
    github_link = models.URLField()
    rank = models.IntegerField()


class Skill(models.Model):
    id = models.UUIDField()
    name = models.CharField()


class Mission(models.Model):
    id = models.UUIDField()
    title = models.CharField()
    about = models.TextField()
    technologies = models.CharField()
    repo_link = models.URLField()
    status = models.CharField()
    tags = models.CharField()
    op = models.CharField()
    recruiting = models.BooleanField()
    rank = models.CharField() #(Duration, members, technologies, )


class Members(models.Model):
    project_id = models.UUIDField()
    user_id = models.UUIDField()
    role = models.CharField()


class Requests(models.Model):
    project_id = models.UUIDField()
    user_id = models.UUIDField()
    type = models.CharField()
    message = models.TextField()


class Feedback(models.Model):
    id = models.UUIDField()
    subject = models.CharField()
    description = models.TextField()
    image = models.ImageField() #1 to many 

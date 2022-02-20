from django.db import models

# Create your models here.
class Skill(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField()


class User(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(password=True)
    name = models.CharField()
    status = models.CharField() 
    profession = models.CharField()
    highest_education = models.CharField()
    college = models.CharField()
    skills = models.ManyToManyField(Skill) # many to many
    about = models.TextField()
    contact_number = models.IntegerField()
    linkedin_link = models.URLField()
    github_link = models.URLField()
    rank = models.IntegerField()


class Mission(models.Model):
    id = models.UUIDField(primary_key=True)
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
    mission_id = models.ForeignKey(Mission, primary_key=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    role = models.CharField()


class Requests(models.Model):
    mission_id = models.ForeignKey(Mission, primary_key=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    type = models.CharField()
    message = models.TextField()


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True)
    subject = models.CharField()
    description = models.TextField()
    image = models.ImageField() #1 to many 

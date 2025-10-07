from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(max_length=500)  # URL for the image
    tags = models.JSONField()  # Store tags as a JSON list
    link = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ContactDetail(models.Model):
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)  # FontAwesome icon class

    def __str__(self):
        return self.type

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=500)
    icon = models.CharField(max_length=100)  # FontAwesome icon class

    def __str__(self):
        return self.name
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True)
    tags = models.JSONField(default=list)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class ContactDetail(models.Model):
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.type

class SocialLink(models.Model):
    link = models.URLField()
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.link

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
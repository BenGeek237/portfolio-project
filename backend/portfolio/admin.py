from django.contrib import admin
from .models import Project, Skill, ContactDetail, SocialLink

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ContactDetail)
admin.site.register(SocialLink)


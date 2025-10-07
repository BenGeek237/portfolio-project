from rest_framework import viewsets
from .models import Project, Skill, ContactDetail, SocialLink
from .serializers import ProjectSerializer, SkillSerializer, ContactDetailSerializer, SocialLinkSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactDetailViewSet(viewsets.ModelViewSet):
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
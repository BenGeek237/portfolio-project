from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Project, Skill, ContactDetail, SocialLink, Message
from .serializers import ProjectSerializer, SkillSerializer, ContactDetailSerializer, SocialLinkSerializer, MessageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

class ContactDetailViewSet(viewsets.ModelViewSet):
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer
    permission_classes = [AllowAny]

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [AllowAny]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]
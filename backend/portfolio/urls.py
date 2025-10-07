from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, ContactDetailViewSet, SocialLinkViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact-details', ContactDetailViewSet)
router.register(r'social-links', SocialLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
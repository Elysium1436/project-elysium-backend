from django.urls import path, include
from .views import ProjectModelViewSet, ProjectImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet, "projects")
router.register(r'images', ProjectImageViewSet, "images")


urlpatterns = [path('', include(router.urls))]
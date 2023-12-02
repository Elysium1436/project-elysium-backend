from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import ProjectMarkdownModel, ProjectImagesModel
from .serializers import ProjectMarkdownSerializer, ProjectImagesSerializer
# Create your views here.


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectMarkdownModel.objects.all()
    serializer_class = ProjectMarkdownSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]

class ProjectImageViewSet(ModelViewSet):
    queryset = ProjectImagesModel.objects.all()
    serializer_class = ProjectImagesSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]
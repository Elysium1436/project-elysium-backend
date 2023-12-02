from rest_framework.serializers import ModelSerializer, ImageField
from .models import ProjectMarkdownModel, ProjectImagesModel




class ProjectMarkdownSerializer(ModelSerializer):

    class Meta:
        model = ProjectMarkdownModel
        fields = '__all__'

class ProjectImagesSerializer(ModelSerializer):
    image = ImageField()

    class Meta:
        model = ProjectImagesModel
        fields = '__all__'
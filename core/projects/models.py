from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class ProjectMarkdownModel(models.Model):
    project_name = models.CharField(max_length=100)
    project_markdown = models.TextField()


class ProjectImagesModel(models.Model):
    image = CloudinaryField("image")

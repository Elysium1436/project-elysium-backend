from django.contrib import admin
from .models import ProjectMarkdownModel, ProjectImagesModel
# Register your models here.

admin.site.register([ProjectMarkdownModel, ProjectImagesModel])

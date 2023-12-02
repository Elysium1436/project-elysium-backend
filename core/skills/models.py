from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class SkillsModel(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_image = CloudinaryField("image", null=True)

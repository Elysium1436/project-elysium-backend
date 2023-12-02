from django.contrib import admin
from .models import SkillsModel
from django.utils.html import format_html
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_image", "image_preview")
    readonly_fields = ["image_preview"]

    @admin.display(description="Image Preview")
    def image_preview(self, obj):
        print(obj.skill_image.build_url(width=100, height=100, crop="thumb"))
        url = obj.skill_image.build_url(width=100, height=100, crop="thumb")
        return format_html('<img src="{}" width="100" height="100"', url)


admin.site.register(SkillsModel, MyModelAdmin)
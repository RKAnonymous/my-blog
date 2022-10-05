from django.contrib import admin
from .models import Technology, Project, Feedback
from .forms import ProjectForm
from django.utils.html import format_html


@admin.register(Technology)
class TechAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo_tag",)
    list_display_links = ("name",)

    def logo_tag(self, obj):
        return format_html(f'<img src="{obj.logo.url}" style="width: 25px; height: 25px" />')

    logo_tag.short_description = "Tech Logo"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ("id", "title", "description", "stacks")
    list_display_links = ("title", )

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

    def stacks(self, obj):
        return "\n".join([p.name for p in obj.stack.all()])

    stacks.short_description = "Stack"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "job", "text", "email")
    list_display_links = ("name", )
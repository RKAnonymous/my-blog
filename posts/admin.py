from django.contrib import admin
from .forms import PostAdminForm
from .models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = ("id", "title", "category_id", "created_at")
    list_display_links = ("title", )
    search_fields = ("title", "category_id", "created_at")


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "post_id", "user_id")
    list_filter = ("user_id", "post_id")
    search_fields = ("text__contains", )


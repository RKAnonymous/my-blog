from django.db import models
from users.models import CustomUser
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from ckeditor.fields import RichTextField


TODAY = now().strftime("%Y_%m_%d_%H_%M")


def category_image_upload_to(instance, filename):
    extension = filename.split('.')[-1]
    if extension not in ['jpg', 'jpeg', 'png']:
        raise ValidationError("Image format is not supported.")

    return "categories/cat_image_" + str(TODAY) + "." + extension


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=category_image_upload_to, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


def post_image_upload_to(instance, filename):
    extension = filename.split('.')[-1]
    if extension not in ['jpg', 'jpeg', 'png']:
        raise ValidationError("Image format is not supported.")

    return "posts/post_image_" + str(TODAY) + "." + extension


class Post(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=200)
    content = RichTextField(max_length=5000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    link = models.URLField(blank=True, null=True, max_length=300)
    image = models.ImageField(upload_to=post_image_upload_to)
    views = models.IntegerField(default=0)


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# Generated by Django 4.0.4 on 2022-04-29 06:37

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.category_image_upload_to),
        ),
    ]
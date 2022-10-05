# Generated by Django 4.0.4 on 2022-04-28 05:18

import ckeditor.fields
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to=main.models.tech_image_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('description_full', ckeditor.fields.RichTextField(max_length=3000)),
                ('logo', models.ImageField(upload_to=main.models.project_image_upload_to)),
                ('link', models.CharField(max_length=200)),
                ('employer', models.CharField(max_length=200)),
                ('pub_date', models.DateField(default='developing')),
                ('team_capacity', models.IntegerField()),
                ('stack', models.ManyToManyField(max_length=50, to='main.technology')),
            ],
        ),
    ]

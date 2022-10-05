from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils.timezone import now


TODAY = now().strftime("%Y_%m_%d_%H_%M")


def tech_image_upload_to(instance, filename):
    extension = filename.split('.')[-1]
    if extension not in ['jpg', 'jpeg', 'png']:
        raise ValidationError("Image format is not supported.")

    return "tech/tech_logo_" + str(TODAY) + "." + extension


class Technology(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=tech_image_upload_to)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


def project_image_upload_to(instance, filename):
    extension = filename.split('.')[-1]
    if extension not in ['jpg', 'jpeg', 'png']:
        raise ValidationError("Image format is not supported.")

    return "projects/projects_image_" + str(TODAY) + "." + extension


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    description_full = RichTextField(max_length=3000)
    logo = models.ImageField(upload_to=project_image_upload_to)
    link = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)
    pub_date = models.DateField(blank=True, null=True)
    is_developing = models.BooleanField(default=False)
    team_capacity = models.IntegerField()
    stack = models.ManyToManyField(Technology, max_length=50)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    email = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)



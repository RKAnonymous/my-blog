# Generated by Django 4.0.4 on 2022-04-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_technology_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_developing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_slug_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
# Generated by Django 4.2.3 on 2023-09-06 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_course_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
    ]

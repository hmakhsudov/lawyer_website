# Generated by Django 4.2.3 on 2023-09-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default=0, max_length=100, verbose_name='Продолжительность'),
            preserve_default=False,
        ),
    ]

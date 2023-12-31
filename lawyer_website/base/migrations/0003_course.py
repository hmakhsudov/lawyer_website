# Generated by Django 4.2.3 on 2023-09-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_testimonial_email_alter_testimonial_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], max_length=20, verbose_name='День недели')),
                ('start_time', models.TimeField(verbose_name='Время начала курса')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('max_students', models.PositiveIntegerField(verbose_name='Максимальное количество студентов')),
                ('enrolled_students_count', models.PositiveIntegerField(default=0, verbose_name='Количество записанных студентов')),
                ('continuation_day', models.CharField(blank=True, choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], max_length=20, null=True, verbose_name='День продолжения курса')),
                ('continuation_time', models.TimeField(blank=True, null=True, verbose_name='Время продолжения курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]

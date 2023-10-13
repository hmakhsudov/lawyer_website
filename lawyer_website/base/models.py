from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.phone}"


class Course(models.Model):
    pass
    # DAY_CHOICES = [
    #     ('Понедельник', 'Понедельник'),
    #     ('Вторник', 'Вторник'),
    #     ('Среда', 'Среда'),
    #     ('Четверг', 'Четверг'),
    #     ('Пятница', 'Пятница'),
    #     ('Суббота', 'Суббота'),
    #     ('Воскресенье', 'Воскресенье'),
    # ]

    # day = models.CharField(max_length=20, choices=DAY_CHOICES, verbose_name='День недели')
    # start_time = models.TimeField(verbose_name='Время начала курса')
    # title = models.CharField(max_length=100, verbose_name='Название курса')
    # description = models.TextField(verbose_name='Описание курса')
    # max_students = models.PositiveIntegerField(verbose_name='Максимальное количество студентов')
    # enrolled_students_count = models.PositiveIntegerField(default=0, verbose_name='Количество записанных студентов')
    # continuation_day_1 = models.CharField(max_length=20, choices=DAY_CHOICES, blank=True, null=True, verbose_name='День продолжения курса 1')
    # continuation_day_2 = models.CharField(max_length=20, choices=DAY_CHOICES, blank=True, null=True, verbose_name='День продолжения курса 2')
    # continuation_time_1 = models.TimeField(blank=True, null=True, verbose_name='Время продолжения курса')
    # continuation_time_2 = models.TimeField(blank=True, null=True, verbose_name='Время продолжения курса')
    # duration = models.CharField(max_length=20, verbose_name='Продолжительность курса')

    # def __str__(self):
    #     return f"{self.get_day_display()} {self.start_time}: {self.title}"

    # class Meta:
    #     verbose_name = 'Курс'
    #     verbose_name_plural = 'Курсы'
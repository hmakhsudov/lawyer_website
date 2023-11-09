from django.db import models
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    name = models.CharField(max_length=255)
    date_starting = models.DateTimeField()
    duration = models.DurationField()  
    limit_of_participants = models.PositiveIntegerField()
    amount_of_participants = models.IntegerField(default=0)
    day_of_week = models.CharField(
        max_length=20,
        choices=[
            ('Понедельник', 'Понедельник'),
            ('Вторник', 'Вторник'),
            ('Среда', 'Среда'),
            ('Четверг', 'Четверг'),
            ('Пятница', 'Пятница'),
            ('Суббота', 'Суббота'),
            ('Воскресенье', 'Воскресенье'),
        ]
    )
    def __str__(self):
        return f"{self.name} - {self.date_starting} - {self.day_of_week}"
    

    
class Enrollment(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    # Add any other fields you might need


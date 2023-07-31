from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.phone}"
    
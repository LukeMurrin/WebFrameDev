from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

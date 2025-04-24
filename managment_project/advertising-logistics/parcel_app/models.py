from django.db import models

class Parcel(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    destination = models.CharField(max_length=255)

    def __str__(self):
        return self.name
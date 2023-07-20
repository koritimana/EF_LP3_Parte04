# mi_aplicacion/models.py

from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    hour = models.IntegerField()
    credits = models.IntegerField()
    state = models.BooleanField()


class Career(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='careers/', null=True, blank=True)
    state = models.BooleanField()

    def __str__(self):
        return self.name







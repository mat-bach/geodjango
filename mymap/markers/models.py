from django.db import models
from django.contrib.gis.db import models


class Marker(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=255)
    location = models.LineStringField()

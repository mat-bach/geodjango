from django.contrib.gis import admin
from .models import Marker, Line


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'location']


@admin.register(Line)
class LineAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'location']

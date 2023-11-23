from django.shortcuts import render
from django.views.generic import TemplateView


class MarkersMapView(TemplateView):
    template_name = 'map.html'

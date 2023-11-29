from django.views.generic import TemplateView
from .models import Marker, Line
from rest_framework import generics
from .serializers import MarkerSerializer, LineSerializer
from rest_framework_gis import filters


class MarkersMapView(TemplateView):
    template_name = 'map.html'


class MarkersAddView(TemplateView):
    template_name = 'add_marker.html'


class LinesAddView(TemplateView):
    template_name = 'add-line.html'


# New marker
class MarkerCreateView(generics.CreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


# Marker list
class MarkerListView(generics.ListAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


class LineCreateView(generics.CreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class LineListView(generics.ListAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    bbox_filter_field = 'location'
    filter_backends = [filters.InBBOXFilter]

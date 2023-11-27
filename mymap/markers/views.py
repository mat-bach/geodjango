from django.views.generic import TemplateView
from .models import Marker
from rest_framework import generics
from .serializers import MarkerSerializer


class MarkersMapView(TemplateView):
    template_name = 'map.html'


class MarkersAddView(TemplateView):
    template_name = 'add_marker.html'


class MarkerCreateView(generics.CreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

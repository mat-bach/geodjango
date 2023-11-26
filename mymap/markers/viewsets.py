from rest_framework import viewsets
from rest_framework_gis import filters
from .models import Marker
from .serializers import MarkerSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = 'location'
    filter_backends = [filters.InBBOXFilter]
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


# class CreateMarkerViewSet(viewsets.ModelViewSet):
#     queryset = Marker.objects.all()
#     serializer_class = MarkerSerializer



from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.core.serializers import serialize
from .models import Marker
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from .serializers import MarkerSerializer


class MarkersMapView(TemplateView):
    template_name = 'map.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     markers = Marker.objects.all()
    #     context['markers'] = json.loads(serialize('geojson', markers))
    #     return context


class MarkersAddView(TemplateView):
    template_name = 'add_marker.html'


# @api_view(['POST'])
# def create_marker(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         data_serializer = MarkerSerializer(data=data)
#         if data_serializer.is_valid():
#             data_serializer.save()
#             return JsonResponse(data_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkerCreateView(generics.CreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

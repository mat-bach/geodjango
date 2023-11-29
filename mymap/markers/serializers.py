from rest_framework_gis import serializers
from .models import Marker, Line


class MarkerSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ['id', 'name']
        geo_field = 'location'
        model = Marker


class LineSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ['id', 'name']
        geo_field = 'location'
        model = Line

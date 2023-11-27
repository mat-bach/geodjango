from django.urls import path
from .views import MarkersMapView, MarkersAddView, MarkerCreateView, MarkerListView

app_name = 'markers'

urlpatterns = [
    path('map/', MarkersMapView.as_view(), name='map'),
    path('map/add_marker', MarkersAddView.as_view(), name='add_marker'),
    path('map/create-marker/', MarkerCreateView.as_view(), name='create-marker'),
    path('map/marker-list/', MarkerListView.as_view(), name='marker-list'),
]

from django.urls import path
from .views import MarkersMapView, MarkersAddView, MarkerCreateView

app_name = 'markers'

urlpatterns = [
    path('map/', MarkersMapView.as_view()),
    path('map/add_marker', MarkersAddView.as_view(), name='add_marker'),
    path('map/create-marker/', MarkerCreateView.as_view(), name='create-marker')
]

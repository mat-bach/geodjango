from django.urls import path
from .views import MarkersMapView, MarkersAddView, MarkerCreateView, MarkerListView, LineListView, LineCreateView
from .views import LinesAddView

app_name = 'markers'

urlpatterns = [
    path('map/', MarkersMapView.as_view(), name='map'),
    path('map/add_marker', MarkersAddView.as_view(), name='add_marker'),
    path('map/add-line', LinesAddView.as_view(), name='add-line'),
    path('map/create-marker/', MarkerCreateView.as_view(), name='create-marker'),
    path('map/create-line/', LineCreateView.as_view(), name='create-line'),
    path('map/marker-list/', MarkerListView.as_view(), name='marker-list'),
    path('map/line-list/', LineListView.as_view(), name='line-list'),
]

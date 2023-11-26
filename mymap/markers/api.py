from rest_framework import routers
from .viewsets import MarkerViewSet
from .views import MarkerCreateView

router = routers.DefaultRouter()
router.register(r'markers', MarkerViewSet)
# router.register(r'markers/add/', MarkerCreateView.as_view(), basename='marker-create')

urlpatterns = router.urls

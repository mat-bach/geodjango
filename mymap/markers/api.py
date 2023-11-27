from rest_framework import routers
from .viewsets import MarkerViewSet
from .views import MarkerCreateView

router = routers.DefaultRouter()
router.register(r'markers', MarkerViewSet)

urlpatterns = router.urls

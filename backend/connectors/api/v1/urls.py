from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137013ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137013", Testconnectors137013ViewSet, basename="testconnectors137013"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

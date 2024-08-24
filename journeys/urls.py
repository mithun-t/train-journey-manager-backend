from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainJourneyViewSet

router = DefaultRouter()
router.register(r'journeys', TrainJourneyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

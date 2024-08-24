from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainJourneyViewSet, StationViewSet, StatusViewSet, BerthViewSet, PaymentModeViewSet

router = DefaultRouter()
router.register(r'journeys', TrainJourneyViewSet)
router.register(r'stations', StationViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'berths', BerthViewSet)
router.register(r'payment_modes', PaymentModeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

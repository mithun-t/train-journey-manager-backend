from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainJourneyViewSet, StationViewSet, StatusViewSet, BerthViewSet, PaymentModeViewSet, UserViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r'journeys', TrainJourneyViewSet, basename='journey')
router.register(r'stations', StationViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'berths', BerthViewSet)
router.register(r'payment_modes', PaymentModeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomObtainAuthToken.as_view()),
]
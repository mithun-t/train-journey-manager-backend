from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainJourneyViewSet, TrainViewSet, StationViewSet, StatusViewSet, BerthViewSet, PaymentModeViewSet, UserViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r'journeys', TrainJourneyViewSet, basename='journey')
router.register(r'trains', TrainViewSet, basename='train')
router.register(r'stations', StationViewSet, basename='station')
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'berths', BerthViewSet, basename='berth')
router.register(r'payment_modes', PaymentModeViewSet, basename='payment_mode')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomObtainAuthToken.as_view()),
]

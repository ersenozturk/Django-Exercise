from rest_framework import routers
from .views import FlightView, ReservationView

router = routers.DefaultRouter()
router.register('flights', FlightView)
router.register('resv', ReservationView)


urlpatterns = [
    # path('', include(router.urls))
]

urlpatterns += router.urls

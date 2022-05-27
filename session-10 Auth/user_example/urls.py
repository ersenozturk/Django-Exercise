from django.urls import path
from .views import home_view, special

urlpatterns = [
    path('', home_view, name="home"),
    path('special', special, name="special"),
]
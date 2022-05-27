from django.urls import path
from .views import home_view, special, register

urlpatterns = [
    path('', home_view, name="home"),
    path('special', special, name="special"),
    path('register', register, name="register"),
]
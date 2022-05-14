from django.urls import path
from .views import home, henry

urlpatterns = [
    path('', home, name='home'),
    path('henry/', henry, name='xyz')
]

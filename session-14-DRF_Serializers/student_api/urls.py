from django.urls import path
from .views import home, path_api, student_api, student_api_get_update_delete

urlpatterns = [
    path('', home),
    path('students/', student_api),
    path('paths/', path_api),
    path('students/<int:pk>', student_api_get_update_delete),
]

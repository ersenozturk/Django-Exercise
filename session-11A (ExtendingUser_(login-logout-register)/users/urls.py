from django.urls import path
from .views import user_logout, user_register,user_login

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('user_login/', user_login, name='user_login'),
]
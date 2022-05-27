from django.urls import path
from .views import home_view, special, register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name="home"),
    path('special', special, name="special"),
    path('register', register, name="register"),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name="change-password"),

]

from django.urls import path
from .views import ContactList, ContactRUD

urlpatterns = [
    path('contact/', ContactList.as_view()),
    path('contact/<int:pk>/', ContactRUD.as_view())
]

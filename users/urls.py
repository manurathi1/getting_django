from .views import register
from django.urls import path

urlpatterns = [
    path('register/', register, name = 'register'),
    # path('register_done/', register_done, name = 'register_done')
]
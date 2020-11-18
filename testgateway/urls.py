from .views import testLandingView, testView
from django.urls import path


urlpatterns = [
    path('', testLandingView, name = 'test_main'),
    path('<slug:slug>', testView, name = 'test_landing'),

    # path('register_done/', register_done, name = 'register_done')
]
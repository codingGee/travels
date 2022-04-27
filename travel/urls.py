from django.urls import path
from .views import HomeView, AboutView, ContactView, ServiceView

app_name = 'travel'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services', ServiceView.as_view(), name='services'),
]

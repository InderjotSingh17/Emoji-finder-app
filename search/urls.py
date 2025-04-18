from django.urls import path
from .views import search_emoji
urlpatterns = [
    path('', search_emoji, name='search_emoji'),
]
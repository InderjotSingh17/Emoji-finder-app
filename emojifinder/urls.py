from django.contrib import admin
from django.urls import path
from search.views import search_emoji

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_emoji),
]

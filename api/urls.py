from django.urls import path
from .views import get_episodes


urlpatterns = [
    path('episodes/', get_episodes, name="episodes-all")
]

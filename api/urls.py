from django.urls import path
from .views import GetEpisodes


urlpatterns = [
    path('episodes/', GetEpisodes.as_view(), name="episodes-all")
]
from rest_framework import generics
from .serializers import EpisodeSerializer
from django.apps import apps

Episode = apps.get_model('episodes', 'Episode')


class GetEpisodes(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
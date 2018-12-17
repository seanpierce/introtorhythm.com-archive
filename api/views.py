from django.apps import apps
from django.core import serializers
from django.http import HttpResponse

Episode = apps.get_model('episodes', 'Episode')

def get_episodes(request):
    """
    Provides a get method handler.
    """
    episodes = Episode.objects.all()
    response = serializers.serialize("json", episodes)
    return HttpResponse(response, content_type='application/json')

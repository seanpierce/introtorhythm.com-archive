import json

from django.apps import apps
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

Episode = apps.get_model('episodes', 'Episode')


class APIResponse():
    def __init__(self, data):
        self.data = data


def response(data):
    return HttpResponse(json.dumps(APIResponse(data).__dict__), content_type='application/json')


def get_episodes(request):
    episodes = Episode.objects.all()
    response = serializers.serialize("json", episodes)
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def create_new_subscription_request(request):
    if request.method == 'POST':
        return response(True)
    else:
        return response(False)

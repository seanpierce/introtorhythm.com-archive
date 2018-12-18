import json
import uuid

from django.apps import apps
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .api_helpers import *

Episode = apps.get_model('episodes', 'Episode')
SubscriptionRequest = apps.get_model('subscribers', 'SubscriptionRequest')


def get_episodes(request):
    episodes = Episode.objects.all()
    response = serializers.serialize("json", episodes)
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def create_new_subscription_request(request):
    if (valid_method('POST', request) == False):
        return error_response(f"Error: Method must be {method}", 405)

    if (valid_header_key(request) == False):
        return error_response("Error: Unauthorized to make request", 401)

    email = request.POST.get('email', False)
    if email == False:
        return error_response("Error: No email provided in request", 422)

    subscription_request, created_new = SubscriptionRequest.objects.get_or_create(
        email=email)

    if created_new == False:
        subscription_request.token = uuid.uuid4()
        subscription_request.save()

    if send_confirmation_email(subscription_request) == True:
        return response(f"Email sent to {email}")
    else:
        return error_response(f"Unable to send email to {email}", 500)

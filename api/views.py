import json

from django.apps import apps
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .api_helpers import APIResponse, send_confirmation_email, response

Episode = apps.get_model('episodes', 'Episode')
SubscriptionRequest = apps.get_model('subscribers', 'SubscriptionRequest')


def get_episodes(request):
    episodes = Episode.objects.all()
    response = serializers.serialize("json", episodes)
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def create_new_subscription_request(request):
    if request.method != 'POST':
        return response("Error: Method must be POST")

    email = request.POST.get('email', False)
    if email == False:
        return response("Error: No email provided in request")

    subscription_request = SubscriptionRequest.objects.get_or_create(
        email=email)

    email_sent = send_confirmation_email(email)

    if email_sent == True:
        return response(f"Email sent to {email}")
    else:
        return response(f"Unable to send email to {email}")

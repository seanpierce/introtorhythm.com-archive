import json

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives


class APIResponse():
    def __init__(self, data):
        self.data = data


def send_confirmation_email(subscription_request):
    subject = 'Confirm your subscription - Intro To Rhythm'
    from_email = 'Intro To Rhythm <noreply@introtorhythm.com>'
    to_email = subscription_request.email
    body = f'Thanks for subscribing! Please confirm your subscription <a href="http://127.0.0.1:8000/api/confirm/?email={subscription_request.email}&token={subscription_request.token}">here</a>'

    try:
        email = EmailMultiAlternatives(subject, "", from_email, [to_email])
        email.attach_alternative(body, "text/html")
        email.send()
        return True
    except:
        return False


def response(data):
    return HttpResponse(json.dumps(APIResponse(data).__dict__), content_type='application/json')


def error_response(data, status):
    return HttpResponse(json.dumps(APIResponse(data).__dict__), content_type='application/json', status=status)


def valid_method(method, request):
    if request.method != method:
        return False
    else:
        return True


def valid_header_key(request):
    secret_key = request.META.get('HTTP_SECRET_KEY', False)

    if secret_key != settings.SUBSCRIBER_KEY:
        return False
    else:
        return True

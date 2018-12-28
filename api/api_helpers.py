import json

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class APIResponse():
    def __init__(self, data):
        self.data = data


def send_confirmation_email(subscription_request):
	context = {
		'email': subscription_request.email,
		'token': subscription_request.token,
    	'host': settings.HOST_URL
	}

	html_content = render_to_string('subscription_confirmation.html', context)

	try:
		send_mail('Please confirm your subsciption to ITR',
			html_content,
			'noreply@introtorhythm.com',
			[subscription_request.email],
			fail_silently=False,
			html_message=html_content)
		return True
	except:
		return False


def response(data):
    return HttpResponse(json.dumps(APIResponse(data).__dict__), content_type='application/json')


def error_response(data, status):
    return HttpResponse(json.dumps(APIResponse(data).__dict__),
		content_type='application/json',
		status=status)


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

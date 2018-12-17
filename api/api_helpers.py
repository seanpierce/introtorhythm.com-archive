import json
import smtplib

from django.http import HttpResponse


class APIResponse():
    def __init__(self, data):
        self.data = data


def send_confirmation_email(email):
    sender = 'noreply@introtorhythm.com'
    receivers = [email]

    message = f"""From: Intro To Rhythm <noreply@introtorhythm.com>
        To: Subscriber <{email}>
        Subject: SMTP e-mail test

        This is a test e-mail message. Ah yee.
        """

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        return True
    except smtplib.SMTPException:
        return False


def response(data):
    return HttpResponse(json.dumps(APIResponse(data).__dict__), content_type='application/json')

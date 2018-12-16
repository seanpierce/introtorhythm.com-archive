import uuid

from django.db import models

# Create your models here.
class Subscriber(models.Model):
	created_at = models.DateTimeField(auto_now=True)
	email = models.EmailField(max_length=255)

	class Meta:
		ordering = ['email',]

	def __str__(self):
		return self.email


class SubscriptionRequest(models.Model):
	created_at = models.DateTimeField(auto_now=True)
	email = models.EmailField(max_length=255)
	token = uuid.uuid4()

	class Meta:
		ordering = ['email',]

	def __str__(self):
		return self.email

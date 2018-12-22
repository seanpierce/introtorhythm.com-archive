from django.contrib import admin

# Register your models here.

from .models import Subscriber, SubscriptionRequest

class SubscriberAdmin(admin.ModelAdmin):
	list_display = ('email', 'created_at')

class SubscriptionRequestAdmin(admin.ModelAdmin):
	list_display = ('token', 'email', 'created_at')

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(SubscriptionRequest, SubscriptionRequestAdmin)

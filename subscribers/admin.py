import csv
from django.contrib import admin
from django.http import HttpResponse
# Register your models here.

from .models import Subscriber, SubscriptionRequest

class SubscriberAdmin(admin.ModelAdmin):
	list_display = ('email', 'created_at')
	actions = ["export_as_csv"]

	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		# field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		# writer.writerow(field_names)
		for obj in queryset:
			writer.writerow([u''.join(obj.email).strip()])

		return response

	export_as_csv.short_description = "Export Selected"

class SubscriptionRequestAdmin(admin.ModelAdmin):
	list_display = ('token', 'email', 'created_at')

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(SubscriptionRequest, SubscriptionRequestAdmin)

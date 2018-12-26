from django.contrib import admin
from .models import Episode

admin.site.site_header = "Intro To Rhythm"
admin.site.site_title = "Intro To Rhythm"
admin.site.index_title = "ITR Admin"

class EpisodeAdmin(admin.ModelAdmin):
	list_display = ('number', 'title', )
	list_per_page = 10

admin.site.register(Episode, EpisodeAdmin)

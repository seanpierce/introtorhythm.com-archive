from django.contrib import admin

admin.site.site_header = "Intro To Rhythm"
admin.site.site_title = "Intro To Rhythm"
admin.site.index_title = "ITR Admin"

from .models import Episode

admin.site.register(Episode)
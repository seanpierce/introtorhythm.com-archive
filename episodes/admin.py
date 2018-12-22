from django.contrib import admin
from .models import Episode

admin.site.site_header = "Intro To Rhythm"
admin.site.site_title = "Intro To Rhythm"
admin.site.index_title = "ITR Admin"

admin.site.register(Episode)

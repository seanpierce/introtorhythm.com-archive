from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	path('live', views.live, name="live"),
	url(r'^$', views.index, name='index'),
	url(r'(?P<primary_key>\d+)$', views.episode, name='episode'),
]

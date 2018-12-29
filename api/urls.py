from django.urls import path
from .views import get_episodes, create_new_subscription_request, create_subscriber, thanks


urlpatterns = [
    path('episodes/', get_episodes, name="episodes_all"),
    path('subscribe/', create_new_subscription_request,
         name="new_subscription_request"),
    path('confirm/', create_subscriber, name='create_subscriber'),
	path('', thanks, name='thanks'),
]

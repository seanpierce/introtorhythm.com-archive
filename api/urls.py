from django.urls import path
from .views import get_episodes, create_new_subscription_request


urlpatterns = [
    path('episodes/', get_episodes, name="episodes-all"),
    path('subscribe/', create_new_subscription_request,
         name="new_subscription_request"),
]

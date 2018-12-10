from rest_framework import serializers
from django.apps import apps

Episode = apps.get_model('episodes', 'Episode')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ("number", "title")
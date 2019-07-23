from rest_framework import serializers
from .models import Songs, Artists


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist", "rating")

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ("firstName", "lastName")

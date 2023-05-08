from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "album_id", "title", "duration"]
        read_only_fields = ["album"]

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

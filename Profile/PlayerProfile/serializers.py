from rest_framework import serializers

from .models import Profile, ScoreStats

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id_hash', 'name']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreStats
        fields = ["user_hash", "score"]





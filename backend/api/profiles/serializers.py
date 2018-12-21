from rest_framework import serializers
from django.contrib.auth.models import User

from backend.app.models import Post

from backend.api.app.serializers import UserSerialiser
from backend.profiles.models import Profile


class ProfileSer(serializers.ModelSerializer):
    """Сериализация профиля"""
    user = UserSerialiser()
    follow = UserSerialiser(many=True)
    class Meta:
        model = Profile
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    """Serializer твитов"""
    user = ProfileSer()
    user_like = UserSerialiser(many=True)
    profile = ProfileSer()
    class Meta:
        model = Post
        fields = ("id",
                  "user",
                  "text",
                  "date",
                  "parent",
                  "like",
                  "user_like",
                  "profile")


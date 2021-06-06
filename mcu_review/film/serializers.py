from django.contrib.auth.models import User

from .models import Film, Review
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class FilmSerializer(serializers.ModelSerializer):
    """ A serializer for the HedgeHog Model """
    class Meta:
        model = Film
        fields = ('id', 'title', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for the Comment model """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'film', 'comment', 'visible', 'created')

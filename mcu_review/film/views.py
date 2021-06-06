from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Film, Comment
from .serializers import UserSerializer, FilmSerializer, CommentSerializer

from rest_framework import serializers
from .models import GroupModel
from apps.users.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = GroupModel
        fields = ('id', 'name', 'description', 'users')

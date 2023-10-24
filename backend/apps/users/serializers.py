from rest_framework.serializers import ModelSerializer, RelatedField

from core.dataclasses.group_dataclass import Group

from .models import UserModel


class GroupUserSerializer(RelatedField):
    def to_representation(self, value: Group):
        return {'id': value.id, 'name': value.name}


class UserSerializer(ModelSerializer):
    # group = GroupUserSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'related_group', 'is_staff',
                  'created_at', 'updated_at'
                  )
        read_only_fields = ('id', 'is_staff',
                            'created_at', 'updated_at')

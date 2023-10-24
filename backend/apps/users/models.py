from django.db import models

from apps.groups.models import GroupModel


class UserModel(models.Model):
    class Meta:
        db_table = 'users'

    email = models.EmailField(unique=True)
    related_group = models.ForeignKey(GroupModel, on_delete=models.PROTECT, related_name='users', null=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





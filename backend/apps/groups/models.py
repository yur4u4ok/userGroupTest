from django.db import models


class GroupModel(models.Model):
    class Meta:
        db_table = 'groups'

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)

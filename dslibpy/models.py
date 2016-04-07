__author__ = 'Darwin Molero (http://darwiniansoftware.com)'

from django.contrib.auth.models import User
from django.db import models


class Entity(models.Model):
    created_by = models.ForeignKey(User, related_name="created_set")
    modified_by = models.ForeignKey(User, related_name="modified_set")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, user, *args, **kwargs):
        if self.id is None:
            self.created_by = self.modified_by = user
        else:
            self.modifield_by = user
        super(Entity, self).save(*args, **kwargs)

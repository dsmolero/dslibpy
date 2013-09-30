__author__ = 'Darwin Molero'

from django.contrib.auth.models import User
from django.db import models

#===============================================================================
class Entity(models.Model):
    #owner = models.ForeignKey(User, related_name="owned_set")
    created_by = models.ForeignKey(User, related_name="created_set")
    modified_by = models.ForeignKey(User, related_name="modified_set")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, user, *args, **kwargs):
        if self.id is None:
            self.created_by = self.modified_by = user
            self.set_owner(user)
        else:
            self.modifield_by = user
        super(Entity, self).save(*args, **kwargs)

    def set_owner(self, user):
        self.owner = user

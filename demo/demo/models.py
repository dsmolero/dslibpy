from django.db import models
from dslibpy.models import Entity


class Issue(Entity):
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

from __future__ import unicode_literals
from django.db import models


class Upload(models.Model):
    """
    Model representing an uploaded file.
    """

    file = models.FileField(upload_to="uploads/")
    filename = models.CharField(max_length=128, blank=True)
    size = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename

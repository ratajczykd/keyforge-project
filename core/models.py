from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)

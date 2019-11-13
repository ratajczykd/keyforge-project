from __future__ import unicode_literals

from django.db import models
import django.contrib.postgres.fields as dcpf


class Player(models.Model):
    name = models.CharField(max_length=50)
    player_no = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    no_of_games = models.IntegerField(default=0)
    previous_oponents = models.CharField(default='0',max_length=50)

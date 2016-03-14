# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

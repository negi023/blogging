from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Types(models.Model):
    types = models.CharField(max_length=20)

    def __str__(self):
        return self.types


class Articles(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Types, default=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, blank=True)
    body = models.TextField()
    thumb = models.ImageField(blank=True, upload_to='post')

    def __str__(self):
        return self.title

    def short(self):
        return self.body[:75] + '...'

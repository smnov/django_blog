from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Author(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

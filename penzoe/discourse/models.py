from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from penzoe.book.models import Book


class Thread(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    comments_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Update timestamps on saving"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Thread, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("thread_comments", kwargs={"id": self.id})


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    text = models.TextField()
    modified = models.DateTimeField()
    comments_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        """Update timestamps on saving"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

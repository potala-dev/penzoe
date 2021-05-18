from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    cover_pg = models.URLField(null=True)
    download_link = models.URLField()
    publish = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"id": self.id})

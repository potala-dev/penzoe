from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    rank = models.IntegerField()
    cover_pg = models.URLField()
    download_link = models.URLField()
    publish = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=250)
    summary = models.TextField()


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'id': self.id})
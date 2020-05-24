from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    profile_pic = models.ImageField(default="default.jpeg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.email} Profile"

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

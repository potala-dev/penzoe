from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

WEIGHTAGE = {
    'book_uploads': 1,
    'threads': 2,
    'comments': 5
}

class User(AbstractUser):
    # upvoted_threads = models.ManyToManyField(Threads, related_name="upvoted_users")
    # downvoted_threads = models.ManyToManyField(Threads, related_name="upvoted_users")
    # upvoted_comments =models.ManyToManyField(Comments, related_name="upvoted_users")
    # upvoted_comments =models.ManyToManyField(Comments, related_name="upvoted_users")
    points = models.IntegerField(default=0)
    data_of_birth_= models.DataField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users/%y/%m/%d/', blank=True)
    background_pic = models.ImageField(upload_to='users/%y/%m/%d/', blank=True)

    def __str__(self):
        return self.email

    def _get_total_points(self, objs):
        return sum([obj.points for obj in objs])


    def update_points(self):
        #threads = self.threads_set.filter(~Q(points = 0))
        #threads_poinst = self._get_total_points(threads) * WEIGHTAGE['threads']
        #comments = self.comments_set.filter(~Q(points = 0))
        #comments_poinst = self._get_total_points(comments) * WEIGHTAGE['comments']
        books_points = self.book_set.count()

        # Calculated weighted points.
        #user_points = n_books_uploaded * WEIGHTAGE['book_uploads'] + threads_points + comments_points
        user_points = books_points * WEIGHTAGE['book_uploads']
        self.points = user_points
        self.save()


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

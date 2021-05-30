from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Word(models.Model):
    form = models.CharField(_("Word form"), max_length=20)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    # SuperMemo2 params
    learning_started = models.DateTimeField(_("Started learning"), auto_now_add=True)
    last_review = models.DateTimeField(_("Last review"), auto_now=True)
    repetitions = models.IntegerField(_("Repetitions"), null=True)
    easiness = models.FloatField("Easiness", null=True)
    next_review = models.DateField("Next review", null=True)
    interval = models.IntegerField("Next review interval", null=True)

    def __str__(self):
        return self.form

    def get_absolute_url(self):
        return reverse("words:detail", kwargs={"pk": self.pk})

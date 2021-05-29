from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from penzoe.quiz.api import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter

# router.register(r"spellquiz", views.SpellFBMCQView)

app_name = "api"
urlpatterns = router.urls

# register non viewset
urlpatterns += [path("quiz/spellmcq/", views.SpellFBMCQView.as_view())]

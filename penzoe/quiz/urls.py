from django.urls import path

from .views import get_spelling_mcq

app_name = "quiz"
urlpatterns = [
    path("spelling-mcq/<str:level>/", view=get_spelling_mcq, name="spelling-mcq")
]

from django.urls import path

from .views import word_detail_view, word_list_view

app_name = "words"
urlpatterns = [
    path("", view=word_list_view, name="list"),
    path("<int:pk>/", view=word_detail_view, name="detail"),
]

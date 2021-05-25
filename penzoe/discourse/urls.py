from django.urls import path

from . import views

app_name = "discourse"
urlpatterns = [
    path("threads/<int:id>/", views.read_threads, name="threads"),
    path("threads/<int:id>/comments", views.thread_comments, name="thread_comments"),
    path("threads/create/<int:id>", views.create_thread, name="thread_create"),
]

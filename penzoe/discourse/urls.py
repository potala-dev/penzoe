from django.urls import path

from . import views

urlpatterns = [
    path("book_threads/<int:id>/", views.book_threads, name="discourse:book_threads"),
    path("threads/<int:id>", views.thread_comments, name="discourse:thread_comments"),
    path(
        "threads/create/<int:id>", views.create_thread, name="discourse:create_thread"
    ),
]

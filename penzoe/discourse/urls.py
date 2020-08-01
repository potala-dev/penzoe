from django.urls import path

from . import views

urlpatterns = [
    path("book_threads/<int:id>/", views.book_threads, name="book_threads"),
    path("threads/<int:id>", views.thread_comments, name="thread_comments"),
    path("threads/create/<int:id>", views.create_thread, name="create_thread"),
]

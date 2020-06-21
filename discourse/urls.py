from django.urls import path

from . import views

urlpatterns = [
    path("book_threads/<int:id>/", views.book_threads, name="book_threads"),
    path("create/<int:id>/", views.create_thread, name="create_thread"),
]

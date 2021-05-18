from django.urls import path

from . import views

urlpatterns = [
    path("", views.book_list, name="home"),
    path("book/<int:id>/", views.book_detail, name="books:book_detail"),
    path("Category/<cat>/", views.book_by_cat, name="books:book_by_cat"),
    path("upload/", views.upload_book, name="books:book_upload"),
]

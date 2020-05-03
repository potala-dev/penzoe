from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('Category/<cat>/', views.book_by_cat, name='book_by_cat'),
]
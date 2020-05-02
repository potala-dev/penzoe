from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('book/<id>/', views.book_detail, name='book_detail')
]
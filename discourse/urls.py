from django.urls import path

from . import views

urlpatterns = [path("create/<int:id>/", views.create_thread, name="create_thread")]

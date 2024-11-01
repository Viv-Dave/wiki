from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.page, name="pages"),
    path("create", views.create, name="create"),
    path("random", views.random, name="random")
]

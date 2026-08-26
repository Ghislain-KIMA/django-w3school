from django.urls import path
from . import views



urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members, name="members"),
    path("members/<slug:slug>/", views.member, name="member"),
    path("testing/", views.testing, name="testing"),
]

from django.urls import path

from .views import BookAPIView

urlspattern = [
    path("", BookAPIView.as_view(), name = "book_list"),
]
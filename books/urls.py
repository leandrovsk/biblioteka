from django.urls import path
from .views import BookView, BookDetailView, FollowingView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("books/<int:pk>/follow/", FollowingView.as_view()),
]

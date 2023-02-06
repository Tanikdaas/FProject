from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view(), name="home"),
    path("<slug:slug>/", views.MovieDetailView.as_view()),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review")
]
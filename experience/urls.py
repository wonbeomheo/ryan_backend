from django.urls import path
from .views import (
    ExperienceListView,
    ExperienceCreateView,
    ExperienceRetrieveView,
    ExperienceUpdateView,
    ExperienceDeleteView,
)

urlpatterns = [
    path("", ExperienceListView.as_view(), name="list"),
    path("register", ExperienceCreateView.as_view(), name="register"),
    path("<int:pk>", ExperienceRetrieveView.as_view(), name="retrieve"),
    path("<int:pk>/update", ExperienceUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", ExperienceDeleteView.as_view(), name="delete"),
]

from django.urls import path
from .views import (
    ExperienceListView,
    ExperienceCreateView,
    ExperienceRetrieveView,
    ExperienceUpdateView,
    ExperienceDeleteView,
)

urlpatterns = [
    path("experiences", ExperienceListView.as_view(), name="list"),
    path("experiences/register", ExperienceCreateView.as_view(), name="register"),
    path("experiences/<int:pk>", ExperienceRetrieveView.as_view(), name="retrieve"),
    path("experiences/<int:pk>/update", ExperienceUpdateView.as_view(), name="update"),
    path("experiences/<int:pk>/delete", ExperienceDeleteView.as_view(), name="delete"),
]

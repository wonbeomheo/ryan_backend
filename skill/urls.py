from django.urls import path
from .views import (
    CategoryListView,
    CategoryRetrieveView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    SkillListView,
    SkillRetrieveView,
    SkillCreateView,
    SkillUpdateView,
    SkillDeleteView,
)

urlpatterns = [
    path("categories", CategoryListView.as_view(), name="list_category"),
    path("categories/<int:pk>", CategoryRetrieveView.as_view(), name="retrieve_category"),
    path("categories/register", CategoryCreateView.as_view(), name="register_category"),
    path("categories/<int:pk>/update", CategoryUpdateView.as_view(), name="update_category"),
    path("categories/<int:pk>/delete", CategoryDeleteView.as_view(), name="delete_category"),
    path("skills", SkillListView.as_view(), name="list"),
    path("skills/<int:pk>", SkillRetrieveView.as_view(), name="retrieve"),
    path("skills/register", SkillCreateView.as_view(), name="register"),
    path("skills/<int:pk>/update", SkillUpdateView.as_view(), name="update"),
    path("skills/<int:pk>/delete", SkillDeleteView.as_view(), name="delete"),
]

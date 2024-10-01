from django.urls import path
from . import views


urlpatterns = [
    path("posts/categories", views.PostCategoryListView.as_view(), name="list_category"),
    path("posts/categories/register", views.PostCategoryCreateView.as_view(), name="register_category"),
    path("posts/categories/<int:pk>", views.PostCategoryRetrieveView.as_view(), name="retrieve_category"),
    path("posts/categories/<int:pk>/update", views.PostCategoryUpdateView.as_view(), name="update_category"),
    path("posts/categories/<int:pk>/delete", views.PostCategoryDeleteView.as_view(), name="delete_category"),
    path("posts", views.PostListView.as_view(), name="list"),
    path("posts/register", views.PostCreateView.as_view(), name="register"),
    path("posts/<int:pk>", views.PostRetrieveView.as_view(), name="retrieve"),
    path("posts/<int:pk>/update", views.PostUpdateView.as_view(), name="update"),
    path("posts/<int:pk>/delete", views.PostDeleteView.as_view(), name="delete"),
]

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PostSerializer, PostCategorySerializer
from .models import Post, PostCategory

class PostCategoryCreateView(CreateAPIView):
    serializer_class = PostCategorySerializer
    permission_classes = [IsAuthenticated]
    

class PostCategoryListView(ListAPIView):
    serializer_class = PostCategorySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return PostCategory.objects.all()
    

class PostCategoryUpdateView(UpdateAPIView):
    serializer_class = PostCategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PostCategory.objects.all()
    

class PostCategoryRetrieveView(RetrieveAPIView):
    serializer_class = PostCategorySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return PostCategory.objects.all()
    

class PostCategoryDeleteView(DestroyAPIView):
    serializer_class = PostCategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PostCategory.objects.all()
    
    
class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    

class PostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Post.objects.all()
    

class PostUpdateView(UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.all()
    

class PostRetrieveView(RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Post.objects.all()
    

class PostDeleteView(DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.all()
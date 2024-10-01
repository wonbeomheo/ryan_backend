from rest_framework.serializers import ModelSerializer
from .models import Post, PostCategory


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        

class PostCategorySerializer(ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"

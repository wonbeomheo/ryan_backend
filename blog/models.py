from django.db import models

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    
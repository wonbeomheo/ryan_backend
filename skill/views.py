from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from .serializers import SkillSerializer, CategorySerializer
from .models import Skill, Category


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    

class CategoryUpdateView(UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.all()


class CategoryDeleteView(DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.all()
    

class CategoryRetrieveView(RetrieveAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Category.objects.all()
    

class SkillListView(ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Skill.objects.all()


class SkillCreateView(CreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    

class SkillUpdateView(UpdateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Skill.objects.all()


class SkillDeleteView(DestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Skill.objects.all()
    

class SkillRetrieveView(RetrieveAPIView):
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Skill.objects.all()
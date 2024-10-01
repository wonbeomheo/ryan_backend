from rest_framework.serializers import ModelSerializer
from .models import Skill, Category


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
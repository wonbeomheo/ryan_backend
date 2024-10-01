from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Experience
from skill.models import Skill
from skill.serializers import SkillSerializer


class ExperienceSerializer(ModelSerializer):
    skills = SerializerMethodField()
    
    class Meta:
        model = Experience
        fields = "__all__"
    
    
    def get_skills(self, obj):
        skills = Skill.objects.filter(skill__experience=obj)
        return SkillSerializer(skills, many=True).data
    
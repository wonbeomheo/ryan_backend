from rest_framework.serializers import ModelSerializer, SerializerMethodField, ListField, DictField, ValidationError
from .models import Experience, ExperienceSkill
from skill.models import Skill, Category
from skill.serializers import SkillSerializer


class ExperienceSerializer(ModelSerializer):
    skills = SerializerMethodField()
    
    class Meta:
        model = Experience
        fields = "__all__"
    
    
    def get_skills(self, obj):
        skills = Skill.objects.filter(skill__experience=obj)
        return SkillSerializer(skills, many=True).data
    
    
class ExperienceCreateSerializer(ModelSerializer):
    skill_list = ListField(
        child=DictField(), write_only=True
    )
    
    class Meta:
        model = Experience
        fields = "__all__"
        
    
    def create(self, validated_data):
        skill_list = validated_data.pop('skill_list', [])
        
        experience = Experience.objects.create(**validated_data)
        
        for skill in skill_list:
            skill_id = skill.get('id', None)
            skill_category = skill.get('category', None)
            if skill_id:
                try:
                    skill_instance = Skill.objects.get(id=skill_id)
                except Exception as e:
                    raise ValidationError(f"Skill with {skill_id} does not exist.")
            else:
                skill_serializer = SkillSerializer(data=skill)
                if skill_serializer.is_valid():
                    try:
                        category = Category.objects.get(id=skill_category)
                    except:
                        raise ValidationError(f"Category with {skill_category} does not exist.")
                    try:
                        skill['category'] = category
                        skill_instance = Skill.objects.create(**skill)
                    except Exception as e:
                        raise ValidationError(e)
                else:
                    raise ValidationError(skill_serializer.errors)
                ExperienceSkill.objects.create(experience=experience, skill=skill_instance)
        return experience
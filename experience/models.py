from django.db import models
from skill.models import Skill


# Create your models here.
class Experience(models.Model):
    company = models.CharField(max_length=255)
    currently_employed = models.BooleanField(default=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    role = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class ExperienceSkill(models.Model):
    experience = models.ForeignKey(Experience, related_name='experience', on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, related_name='skill', on_delete=models.PROTECT)
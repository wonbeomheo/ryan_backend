from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    CategoryOptions = {
        "TS": "Technical Skills",
        "SS": "Soft Skills"
    }
    name = models.CharField(max_length=2, choices=CategoryOptions, unique=True)
    
    def __str__(self):
        return self.CategoryOptions[self.name]
    
class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    
    
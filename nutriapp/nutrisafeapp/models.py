from django.db import models

# myapp/models.py


from django.contrib.auth.models import User

from .models import UserProfile

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields related to user profile (e.g., age, location, etc.)

class NutritionalIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=100)
    calories = models.IntegerField()
    # Add other fields for nutritional tracking (e.g., date, nutrients, etc.)



class FoodSource(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # Add other fields related to the food source (e.g., type, description, etc.)
    
    
class Meal(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=100)
    calories = models.IntegerField()

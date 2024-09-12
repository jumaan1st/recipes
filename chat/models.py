from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    cuisine = models.ForeignKey(Cuisine, related_name='recipes', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    preparation_time = models.PositiveIntegerField()  # Time in minutes
    cooking_time = models.PositiveIntegerField()  # Time in minutes
    serves = models.PositiveIntegerField()

    def __str__(self):
        return self.name

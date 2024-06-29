from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    objects: models.Manager()

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    cooking_method = models.TextField()
    cooking_time = models.TimeField()
    image = models.ImageField(upload_to='myproject/media/img/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects: models.Manager()

    def __str__(self) -> str:
        return self.title

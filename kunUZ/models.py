import datetime

from django.db import models


# Create your models here.

class Yangiliklar(models.Model):
    title = models.CharField(max_length=355)
    slug = models.SlugField(unique=True)
    paragraph = models.TextField()
    description = models.TextField()
    dolzarb = models.BooleanField(default=False)
    songgi_yangiliklar = models.BooleanField(default=False)
    pub_year = datetime.datetime.now().strftime("%H:%M / %d.%m.%Y")
    video = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category")
    region = models.ForeignKey("Region", on_delete=models.CASCADE, related_name="region")

class Region(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

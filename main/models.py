from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
    ]

    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices= CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    



    
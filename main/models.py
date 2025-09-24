from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'jersey'),
        ('full jersey', 'full jersey'),
        ('pants', 'pants')

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices= CATEGORY_CHOICES, max_length=50)
    is_featured = models.BooleanField(default=False)
    product_sold = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_product_popular(self):
        return self.product_sold > 30
    
    def increment_product_sold(self):
        self.product_sold += 1
        self.save()


    



    
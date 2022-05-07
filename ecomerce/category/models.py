from email.mime import image
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    slug = models.CharField(max_length=100 , unique=True)
    description = models.TextField(max_length=255 , blank=True)
    image = models.ImageField(upload_to='images/categories',blank=True)

    # class Meta:
    #     db_table = "category"

    def __str__(self) -> str:
        return self.name

from email.mime import image
from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField(max_length=255 , blank=True)
    image = models.ImageField(upload_to='images/categories',blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    #     db_table = "category"

    def __str__(self) -> str:
        return self.name

from operator import truediv
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Catrgories"
        ordering = ['-created_at']



class Photo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, null=True,   on_delete=models.SET_NULL)
    image = models.ImageField(null=False,upload_to='static/images', blank=False)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.created_at}"
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Catalogue(models.Model):
    category = models.ForeignKey(Category, related_name='catalog_items', on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='NA')
    name = models.CharField(max_length=255)
    quantity=models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    sell_or_donate=models.CharField(max_length=255)
    price = models.FloatField()
    negotiable_price = models.BooleanField(default=True)
    location = models.CharField(max_length=255, default='Delhi')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    seller_name = models.CharField(max_length=255, default='NA')
    email = models.CharField(max_length=255, default='NA')
    mobile = models.IntegerField()
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='seller_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    location = models.CharField(max_length=255, default='Delhi')
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    negotiable_price = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Donator(models.Model):
    seller_name = models.CharField(max_length=255, default='NA')
    email = models.CharField(max_length=255, default='NA')
    mobile = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='donator_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    location = models.CharField(max_length=255, default='Delhi')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name

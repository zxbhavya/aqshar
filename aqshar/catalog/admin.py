from django.contrib import admin

from .models import Category, Catalogue, Seller, Donator

admin.site.register(Category)
admin.site.register(Catalogue)
admin.site.register(Seller)
admin.site.register(Donator)
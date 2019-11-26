from django.contrib import admin
from .models import Profile, Order, Item, Product

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Item)
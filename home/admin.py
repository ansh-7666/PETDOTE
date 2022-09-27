from django.contrib import admin
from home.models import Product,order,ordered_items

# Register your models here.
admin.site.register(Product)
admin.site.register(order)
admin.site.register(ordered_items)
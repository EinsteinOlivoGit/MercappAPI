from django.contrib import admin
from .models import Market, Item, Purchase, Item_purchase
# Register your models here.

admin.site.register(Market)
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(Item_purchase)
from django.db import models
from django.contrib.auth.models import User

class Market(models.Model):
    name = models.CharField(max_length=80)
    slogan = models.CharField(max_length=200)
    create_date = models.DateField()
    last_update_date = models.DateField()
    users = models.ManyToManyField(User)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    create_date = models.DateField()
    last_update_date = models.DateField()
    users = models.ManyToManyField(User)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='Item_purchase')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_with_taxes = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateField()
    last_update_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    state = models.CharField(max_length=2)

    
class Item_purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_with_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_date = models.DateField()
    last_update_date = models.DateField()
    state = models.CharField(max_length=2)


# Generated by Django 3.0.3 on 2020-03-02 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_item_item_purchase_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_purchase',
            name='price_with_taxes',
        ),
        migrations.RemoveField(
            model_name='item_purchase',
            name='users',
        ),
        migrations.AddField(
            model_name='item_purchase',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item_purchase',
            name='purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase.Purchase'),
        ),
        migrations.AddField(
            model_name='item_purchase',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='item_purchase',
            name='total_with_taxes',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='purchase',
            name='items',
            field=models.ManyToManyField(through='purchase.Item_purchase', to='purchase.Item'),
        ),
        migrations.AlterField(
            model_name='item_purchase',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase.Item'),
        ),
        migrations.AlterField(
            model_name='item_purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

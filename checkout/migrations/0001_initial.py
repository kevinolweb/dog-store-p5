# Generated by Django 3.2.20 on 2023-09-03 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20230711_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=200)),
                ('order_number', models.CharField(editable=False, max_length=35)),
                ('postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('town_or_city', models.CharField(max_length=45)),
                ('street_address1', models.CharField(max_length=70)),
                ('street_address2', models.CharField(blank=True, max_length=70, null=True)),
                ('county', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_items', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]

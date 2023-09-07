# Generated by Django 3.2.20 on 2023-09-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230711_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='alt_tag',
            field=models.CharField(blank=True, max_length=61, null=True),
        ),
    ]

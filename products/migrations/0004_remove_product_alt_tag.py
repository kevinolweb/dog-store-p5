# Generated by Django 3.2.20 on 2023-09-07 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230907_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='alt_tag',
        ),
    ]
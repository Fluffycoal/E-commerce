# Generated by Django 5.1.3 on 2024-11-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.CharField(default='Default Product', max_length=255),
        ),
    ]

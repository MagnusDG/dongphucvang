# Generated by Django 5.0.1 on 2024-01-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Số điện thoại'),
        ),
    ]

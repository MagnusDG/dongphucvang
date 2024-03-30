# Generated by Django 5.0.1 on 2024-01-12 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_order_expected_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='all_unit_price',
            field=models.FloatField(default=0, verbose_name='Thành tiền'),
        ),
        migrations.AddField(
            model_name='order',
            name='vat_price',
            field=models.FloatField(default=0, verbose_name='VAT'),
        ),
    ]
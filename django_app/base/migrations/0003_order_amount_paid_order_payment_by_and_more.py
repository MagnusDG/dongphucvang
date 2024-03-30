# Generated by Django 5.0.1 on 2024-01-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_customer_address_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_paid',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('COD', 'COD'), ('ATM/E-banking', 'ATM/E-banking'), ('Tiền mặt', 'Tiền mặt'), ('Momo', 'Momo'), ('Zalo Pay', 'Zalo Pay'), ('Thẻ tín dụng', 'Thẻ tín dụng'), ('VNPAY', 'VNPAY')], default='Đang xử lý', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Chưa thanh toán', 'Chưa thanh toán'), ('Đã thanh toán', 'Đã thanh toán'), ('Đã thanh toán một phần', 'Đã thanh toán một phần')], default='Đang xử lý', max_length=50),
        ),
    ]

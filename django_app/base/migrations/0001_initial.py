# Generated by Django 4.2.4 on 2023-09-05 17:17

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Họ KH', max_length=50)),
                ('last_name', models.CharField(default='Tên KH', max_length=50)),
                ('phone_number', models.CharField(default='SĐT KH', max_length=15, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default=base.models.generate_order_id, max_length=10, unique=True)),
                ('name', models.CharField(default='Tên ĐH', max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Đang xử lý', 'Đang xử lý'), ('Đang sản xuất', 'Đang sản xuất'), ('Đang giao hàng', 'Đang giao hàng'), ('Hoàn tất', 'Hoàn tất'), ('Đã hủy', 'Đã hủy')], default='Đang xử lý', max_length=20)),
                ('size_xs_quantity', models.PositiveIntegerField(default=0)),
                ('size_s_quantity', models.PositiveIntegerField(default=0)),
                ('size_m_quantity', models.PositiveIntegerField(default=0)),
                ('size_l_quantity', models.PositiveIntegerField(default=0)),
                ('size_xl_quantity', models.PositiveIntegerField(default=0)),
                ('size_xxl_quantity', models.PositiveIntegerField(default=0)),
                ('size_3xl_quantity', models.PositiveIntegerField(default=0)),
                ('style', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('neck', models.CharField(max_length=50)),
                ('hand', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('has_logo', models.BooleanField(default=False)),
                ('custom_logo', models.ImageField(blank=True, null=True, upload_to='custom_shirt_logos/')),
                ('custom_logo_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

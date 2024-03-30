# Generated by Django 5.0.1 on 2024-01-11 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_order_prodplant_alter_order_color_alter_order_hand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completeed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày hoàn thành'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày giao hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Màu sắc'),
        ),
        migrations.AlterField(
            model_name='order',
            name='custom_logo',
            field=models.ImageField(blank=True, null=True, upload_to='custom_shirt_logos/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='custom_logo_url',
            field=models.URLField(blank=True, null=True, verbose_name='Link logo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='hand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tay'),
        ),
        migrations.AlterField(
            model_name='order',
            name='material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Chất liệu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Tên đơn hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='neck',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cổ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prodPlant',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='SX'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Đang xử lý', 'Đang xử lý'), ('Đã cọc', 'Đã cọc'), ('Đã sản xuất', 'Đã sản xuất'), ('Đã giao', 'Đã giao'), ('Đã hủy', 'Đã hủy')], default='Đang xử lý', max_length=20, verbose_name='Trạng thái đơn hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='style',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kiểu dáng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Tổng tiền'),
        ),
        migrations.AlterField(
            model_name='order',
            name='unit_price',
            field=models.FloatField(default=0, verbose_name='Đơn giá'),
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone





#------------------------------------------------------------#
def generate_order_id():
    now = timezone.now()
    year = now.strftime('%y')
    month = now.strftime('%m')
    last_order = Order.objects.filter(order_id__contains=f'{year}-{month}').order_by('-order_id').first()
    
    if last_order:
        last_id = int(last_order.order_id.split('-')[-1])
        new_id = last_id + 1
    else:
        new_id = 1
    
    return f'{year}-{month}-{new_id:03}'

#------------------------------------------------------------#
class Customer(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Tên khách hàng')
    last_name = models.CharField(max_length=50, verbose_name='Họ khách hàng')
    phone_number = models.CharField(max_length=15, verbose_name='Số điện thoại')
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='Email')
    address = models.TextField(blank=True, null=True, verbose_name='Địa chỉ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#------------------------------------------------------------#
class Order(models.Model):
    STATUS_CHOICES = (
        ('Đang xử lý', 'Đang xử lý'),
        ('Đã cọc', 'Đã cọc'),
        ('Đã sản xuất', 'Đã sản xuất'),
        ('Đã giao', 'Đã giao'),
        ('Đã hủy', 'Đã hủy'),
    )
    order_id = models.CharField(max_length=10, unique=True, default=generate_order_id)
    name = models.CharField(max_length=100, verbose_name='Tên đơn hàng')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Trạng thái đơn hàng', default='Đang xử lý')

    freesize = models.BooleanField(default=False)

    size_xs_quantity = models.PositiveIntegerField(default=0)
    size_s_quantity = models.PositiveIntegerField(default=0)
    size_m_quantity = models.PositiveIntegerField(default=0)
    size_l_quantity = models.PositiveIntegerField(default=0)
    size_xl_quantity = models.PositiveIntegerField(default=0)
    size_xxl_quantity = models.PositiveIntegerField(default=0)
    size_3xl_quantity = models.PositiveIntegerField(default=0)

    male_size_xs_quantity = models.PositiveIntegerField(default=0)
    male_size_s_quantity = models.PositiveIntegerField(default=0)
    male_size_m_quantity = models.PositiveIntegerField(default=0)
    male_size_l_quantity = models.PositiveIntegerField(default=0)
    male_size_xl_quantity = models.PositiveIntegerField(default=0)
    male_size_xxl_quantity = models.PositiveIntegerField(default=0)
    male_size_3xl_quantity = models.PositiveIntegerField(default=0)
    
    female_size_xs_quantity = models.PositiveIntegerField(default=0)
    female_size_s_quantity = models.PositiveIntegerField(default=0)
    female_size_m_quantity = models.PositiveIntegerField(default=0)
    female_size_l_quantity = models.PositiveIntegerField(default=0)
    female_size_xl_quantity = models.PositiveIntegerField(default=0)
    female_size_xxl_quantity = models.PositiveIntegerField(default=0)
    female_size_3xl_quantity = models.PositiveIntegerField(default=0)

    STYLE_CHOICES = (
        ('Cổ bẻ', 'Cổ bẻ'),
        ('Cổ trụ', 'Cổ trụ'),
        ('Cổ tim', 'Cổ tim'),
        ('Cổ tròn', 'Cổ tròn'),
        ('Cổ V', 'Cổ V'),
        ('Cổ chữ U', 'Cổ chữ U'),
        ('Cổ sơ mi', 'Cổ sơ mi'),
        ('Cổ đức', 'Cổ đức'),
    )

    MATERIAL_CHOICES = (
        ('Cotton', 'Cotton'),
        ('Lụa', 'Lụa'),
        ('Kaki', 'Kaki'),
        ('Jeans', 'Jeans'),
        ('Lanh', 'Lanh'),
        ('Thun', 'Thun'),
        ('Nỉ', 'Nỉ'),
        ('Vải dù', 'Vải dù'),
        ('Vải mưa', 'Vải mưa'),
    )

    style = models.CharField(max_length=50, choices=STYLE_CHOICES, verbose_name='Kiểu dáng', default='Cổ bẻ')
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Màu sắc')
    collar = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bo cổ/tay')
    pillar = models.CharField(max_length=50, blank=True, null=True, verbose_name='Trụ áo')
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES, verbose_name='Chất liệu', default='Cotton')

    custom_logo = models.ImageField(upload_to='custom_shirt_logos/', blank=True, null=True, verbose_name='Logo')
    custom_logo_url = models.URLField(blank=True, null=True, verbose_name='Link logo')
 
    prodPlant = models.CharField(max_length=50, blank=True, null=True, verbose_name='SX')
    PAYMENT_STATUS_CHOICES = (
        ('Chưa thanh toán', 'Chưa thanh toán'),
        ('Đã thanh toán', 'Đã thanh toán'),
        ('Đã thanh toán một phần', 'Đã thanh toán một phần'),
    )


    unit_price = models.FloatField(default=0, verbose_name='Đơn giá')
    total_price_vat = models.FloatField(default=0, verbose_name='Thành tiền')
    vat = models.FloatField(default=0.08, verbose_name='VAT')
    vat_price = models.FloatField(default=0, verbose_name='VAT')
    total_price = models.FloatField(default=0, verbose_name='Tổng tiền')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='Đang xử lý')
    paid = models.FloatField(default=0)
    unpaid = models.FloatField(default=0)

    expected_date = models.PositiveIntegerField(default=0)
    completed_date = models.DateTimeField(blank=True, null=True, verbose_name='Ngày hoàn thành')
    delivered_date = models.DateTimeField(blank=True, null=True, verbose_name='Ngày giao hàng')

    @property
    def total_quantity_male(self):
        return (
                self.male_size_xs_quantity +
                self.male_size_s_quantity +
                self.male_size_m_quantity +
                self.male_size_l_quantity +
                self.male_size_xl_quantity +
                self.male_size_xxl_quantity +
                self.male_size_3xl_quantity 
            )
    def total_quantity_female(self):
        return (
            self.female_size_xs_quantity +
                self.female_size_s_quantity +
                self.female_size_m_quantity +
                self.female_size_l_quantity +
                self.female_size_xl_quantity +
                self.female_size_xxl_quantity +
                self.female_size_3xl_quantity
        )



    @property
    def total_quantity(self):
        # Tính tổng số lượng từng kích thước
        if self.freesize:
            return (
                self.size_xs_quantity +
                self.size_s_quantity +
                self.size_m_quantity +
                self.size_l_quantity +
                self.size_xl_quantity +
                self.size_xxl_quantity +
                self.size_3xl_quantity
            )
        else:
            return (
                self.male_size_xs_quantity +
                self.male_size_s_quantity +
                self.male_size_m_quantity +
                self.male_size_l_quantity +
                self.male_size_xl_quantity +
                self.male_size_xxl_quantity +
                self.male_size_3xl_quantity +
                self.female_size_xs_quantity +
                self.female_size_s_quantity +
                self.female_size_m_quantity +
                self.female_size_l_quantity +
                self.female_size_xl_quantity +
                self.female_size_xxl_quantity +
                self.female_size_3xl_quantity
            )


    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_order_id()

        # Calculate all_unit_price based on unit_price and total_quantity
        self.total_price = self.unit_price * self.total_quantity

        # Calculate VAT price separately based on total_price and vat rate
        self.vat_price = self.unit_price * self.total_quantity * self.vat

        # Calculate total_price_vat including VAT
        self.total_price_vat = self.unit_price * self.total_quantity + self.unit_price * self.total_quantity * self.vat

        # Call the original save method
        super(Order, self).save(*args, **kwargs)



    def __str__(self):
        return f"Custom Shirt Order {self.order_id}"


def get_image_filename(instance, filename):
    order_id = instance.order.order_id
    return f'custom_shirt_images/{order_id}/{filename}'
def get_image_filename2(instance, filename):
    ReferenceError.add_note()

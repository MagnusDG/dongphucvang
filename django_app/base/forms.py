from django import forms
from .models import Customer, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'status', 'freesize', 'size_xs_quantity', 'size_s_quantity', 'size_m_quantity', 'size_l_quantity', 'size_xl_quantity', 'size_xxl_quantity', 'size_3xl_quantity', 'male_size_xs_quantity', 'male_size_s_quantity', 'male_size_m_quantity', 'male_size_l_quantity', 'male_size_xl_quantity', 'male_size_xxl_quantity', 'male_size_3xl_quantity', 'female_size_xs_quantity', 'female_size_s_quantity', 'female_size_m_quantity', 'female_size_l_quantity', 'female_size_xl_quantity', 'female_size_xxl_quantity', 'female_size_3xl_quantity', 'style', 'color', 'collar', 'pillar', 'material', 'custom_logo', 'custom_logo_url', 'unit_price', 'delivered_date']
        widgets = {
            'unit_price': forms.NumberInput(attrs={'id': 'unit-price-input'}),
        }
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Đặt id cho các trường size
        self.fields['size_xs_quantity'].widget.attrs['id'] = 'size_xs_quantity_field'
        self.fields['size_s_quantity'].widget.attrs['id'] = 'size_s_quantity_field'
        self.fields['size_m_quantity'].widget.attrs['id'] = 'size_m_quantity_field'
        self.fields['size_l_quantity'].widget.attrs['id'] = 'size_l_quantity_field'
        self.fields['size_xl_quantity'].widget.attrs['id'] = 'size_xl_quantity_field'
        self.fields['size_xxl_quantity'].widget.attrs['id'] = 'size_xxl_quantity_field'
        self.fields['size_3xl_quantity'].widget.attrs['id'] = 'size_3xl_quantity_field'
        # ... (tương tự cho các trường size khác)
        self.fields['male_size_xs_quantity'].widget.attrs['id'] = 'male_size_xs_quantity_field'
        self.fields['male_size_s_quantity'].widget.attrs['id'] = 'male_size_s_quantity_field'
        self.fields['male_size_m_quantity'].widget.attrs['id'] = 'male_size_m_quantity_field'
        self.fields['male_size_l_quantity'].widget.attrs['id'] = 'male_size_l_quantity_field'
        self.fields['male_size_xl_quantity'].widget.attrs['id'] = 'male_size_xl_quantity_field'
        self.fields['male_size_xxl_quantity'].widget.attrs['id'] = 'male_size_xxl_quantity_field'
        self.fields['male_size_3xl_quantity'].widget.attrs['id'] = 'male_size_3xl_quantity_field'
        # ... (tương tự cho các trường size nam khác)
        self.fields['female_size_xs_quantity'].widget.attrs['id'] = 'feale_size_xs_quantity_field'
        self.fields['female_size_s_quantity'].widget.attrs['id'] = 'female_size_s_quantity_field'
        self.fields['female_size_m_quantity'].widget.attrs['id'] = 'female_size_m_quantity_field'
        self.fields['female_size_l_quantity'].widget.attrs['id'] = 'female_size_l_quantity_field'
        self.fields['female_size_xl_quantity'].widget.attrs['id'] = 'female_size_xl_quantity_field'
        self.fields['female_size_xxl_quantity'].widget.attrs['id'] = 'female_size_xxl_quantity_field'
        self.fields['female_size_3xl_quantity'].widget.attrs['id'] = 'female_size_3xl_quantity_field'
        # ... (tương tự cho các trường size nữ khác)
        


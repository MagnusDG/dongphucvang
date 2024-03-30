from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView
from .forms import OrderForm, CustomerForm
from .models import Order, Customer, User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from django.template.loader import render_to_string
import pdfkit, tempfile, os



def httpError(request):
    return HttpResponse("Error 404")







@login_required(login_url='login')
def order(request, pk):
    order = Order.objects.get(id=pk)
    total_quantity = order.total_quantity  # Tính toán total_quantity từ thuộc tính của đối tượng Order
    total_quantity_male = order.total_quantity_male
    total_quantity_female = order.total_quantity_female
    context = {
        'order': order,
        'total_quantity': total_quantity  # Đưa total_quantity vào context
    }

    return render(request, 'base/order.html', context)


def get_orders(request):
    orders = Order.objects.all()

    style = request.GET.get('style_filter', '')
    material = request.GET.get('material_filter', '')
    color = request.GET.get('color_filter', '')
    printing = request.GET.get('print_filter', '')

    if style != 'Tất cả':
        orders = orders.filter(style=style)

    if material != 'Tất cả':
        orders = orders.filter(material=material)

    if color != '':
        orders = orders.filter(color=color)

    if printing != '':
        orders = orders.filter(printing=printing)

    return orders



# Trang chủ
@login_required(login_url='login')
def home(request):
    selected_month = None

    if request.method == 'GET':
        selected_month_str = request.GET.get('selected_month')
        if selected_month_str:
            selected_month = datetime.strptime(selected_month_str, "%Y-%m")

    orders = get_orders(request)  # Lấy danh sách đơn hàng đã được lọc

    if selected_month:
        orders = orders.filter(
            created__month=selected_month.month,
            created__year=selected_month.year,
        )

    context = {'orders': orders, 'selected_month': selected_month}

    return render(request, 'base/home.html', context)


def employee_orders(request):
    current_user = request.user  # Lấy thông tin người dùng hiện tại từ request

    selected_month_str = request.GET.get('selected_month')
    selected_month = None

    if selected_month_str:
        selected_month = datetime.strptime(selected_month_str, "%Y-%m")

    orders = None
    if selected_month:
        orders = Order.objects.filter(
            created__month=selected_month.month,
            created__year=selected_month.year,
            user=current_user  # Thay `user` bằng trường chứa thông tin người dùng trong model Order của bạn
        )
    else:
        orders = Order.objects.filter(user=current_user)  # Tương tự, thay `user` bằng trường chứa thông tin người dùng trong model Order của bạn

    return render(request, 'base/employee_orders.html', {'orders': orders})







class LoginView(LoginView):
    template_name = 'base/login.html'  # Đường dẫn đến template đăng nhập
    success_url = reverse_lazy('base/home.html')  # Đường dẫn sau khi đăng nhập thành công



# Tạo đơn hàng
@login_required(login_url='login')
def create_order(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        
        if customer_form.is_valid() and order_form.is_valid():
            phone_number = customer_form.cleaned_data['phone_number']
            customer = None

            # Kiểm tra xem thông tin khách hàng đã tồn tại hay chưa
            try:
                customer = Customer.objects.get(phone_number=phone_number)
            except Customer.DoesNotExist:
                # Nếu không tìm thấy khách hàng, tạo khách hàng mới từ form
                customer = Customer.objects.create(phone_number=phone_number, first_name=customer_form.cleaned_data['first_name'], last_name=customer_form.cleaned_data['last_name'], address=customer_form.cleaned_data['address'], email=customer_form.cleaned_data['email'])

            # Tạo đơn hàng và liên kết với thông tin khách hàng
            order = order_form.save(commit=False)
            order.customer = customer
            order.user = request.user  # Thay bằng user hiện tại hoặc xử lý tùy theo cách bạn quản lý người dùng
            order.save()

            return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang thành công
    else:
        customer_form = CustomerForm()
        order_form = OrderForm()

    
    return render(request, 'base/create_order.html', {'customer_form': customer_form, 'order_form': order_form})













def employee_orders(request):
    current_user = request.user  # Lấy thông tin người dùng hiện tại từ request

    selected_month_str = request.GET.get('selected_month')
    selected_month = None

    if selected_month_str:
        selected_month = datetime.strptime(selected_month_str, "%Y-%m")

    orders = None
    if selected_month:
        orders = Order.objects.filter(
            created__month=selected_month.month,
            created__year=selected_month.year,
            user=current_user  # Thay `user` bằng trường chứa thông tin người dùng trong model Order của bạn
        )
    else:
        orders = Order.objects.filter(user=current_user)  # Tương tự, thay `user` bằng trường chứa thông tin người dùng trong model Order của bạn

    return render(request, 'base/employee_orders.html', {'orders': orders})





def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # Chuyển hướng hoặc thông báo cập nhật đơn hàng thành công
        return redirect('order', pk=order_id)  # Thay 'order_detail' bằng tên URL pattern của trang chi tiết đơn hàng

    else:
        form = OrderForm(instance=order)
    
    return render(request, 'base/edit_order.html', {'form': form, 'order': order})



def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('home')  # Chuyển hướng về trang home sau khi xóa đơn hàng

# def print_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     context = {'order': order}

#     # Render template to HTML
#     html_content = render_to_string('base/print_order_template.html', context)

#     # Create response as a PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename=order_{order_id}.pdf'

#     # Specify the path to wkhtmltopdf executable (change the path accordingly)
#     config = pdfkit.configuration(wkhtmltopdf="D:/WebAppPJ/order_management/wkhtmltopdf/bin/wkhtmltopdf.exe")

#     # PDF rendering using pdfkit with configuration
#     pdfkit.from_string(html_content, response, configuration=config)

#     return response




def print_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}

    # Render template to HTML
    html_content = render_to_string('base/print_order_template.html', context)

   
    # Create PDF using pdfkit with the specified configuration
    config = pdfkit.configuration(wkhtmltopdf='D:/WebAppPJ/order_management/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(str(html_content), 'base/temp.pdf',options={"enable-local-file-access": ""}, configuration=config)

    # Open the temporary file in binary mode and read its content
    with open('base/temp.pdf', 'rb') as pdf_file:
        # Create response as a PDF
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'filename=order_{order_id}.pdf'

    os.remove('base/temp.pdf')
    return response


def print_mo(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}

    # Render template to HTML
    html_content = render_to_string('base/print_mo_template.html', context)

   
    # Create PDF using pdfkit with the specified configuration
    config = pdfkit.configuration(wkhtmltopdf='D:/WebAppPJ/order_management/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(str(html_content), 'base/tempMO.pdf',options={"enable-local-file-access": ""}, configuration=config)

    # Open the temporary file in binary mode and read its content
    with open('base/tempMO.pdf', 'rb') as pdf_file:
        # Create response as a PDF
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'filename=Lenh_SX_{order_id}.pdf'

    os.remove('base/tempMO.pdf')
    return response
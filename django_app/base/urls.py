from django.urls import path
from . import views
from .views import LoginView



urlpatterns = [
    path('', views.home, name="home"),
    path('order/<str:pk>', views.order, name="order"),
    path('login/', LoginView.as_view(), name='login'),
    path('create-order/', views.create_order, name='create-order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('employee_orders/', views.employee_orders, name='employee_orders'),
    path('print_order/<int:order_id>/', views.print_order, name='print_order'),
    path('print_mo/<int:order_id>/', views.print_mo, name='print_mo'),

]
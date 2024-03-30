$(document).ready(function() {
    $("#month-picker").datepicker({
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        dateFormat: 'yy-mm', // Định dạng ngày: năm-tháng
        onClose: function(dateText, inst) {
            var selectedDate = $(this).datepicker('getDate');
            if (selectedDate) {
                var year = selectedDate.getFullYear();
                var month = selectedDate.getMonth() + 1;
                // Gọi hàm AJAX để tìm đơn hàng theo tháng
                fetchOrdersByMonth(year, month);
            }
        }
    });
});

function fetchOrdersByMonth(year, month) {
    $.ajax({
        url: '/api/orders/', // Điều hướng API của bạn để lấy danh sách đơn hàng
        method: 'GET',
        data: {
            year: year,
            month: month
        },
        success: function(data) {
            // Xử lý dữ liệu trả về (hiển thị danh sách đơn hàng)
            console.log(data); // Dữ liệu trả về từ máy chủ Django
        },
        error: function(error) {
            console.log('Lỗi khi tải danh sách đơn hàng:', error);
        }
    });
}
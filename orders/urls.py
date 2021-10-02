from django.urls import path
from .views import order_create, detail, payment, verify, coupon_apply

app_name = 'orders'
urlpatterns = [
	path('/create/', order_create, name='create'),
	path('/<int:order_id>/', detail, name='detail'),
	path('/payment/<price>/', payment, name='payment'),
	path('verify/', verify, name='verify'),
	path('apply/<int:order_id>/', coupon_apply, name='coupon_apply' ),
]
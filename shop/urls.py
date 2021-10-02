from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', home, name='category_filter'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
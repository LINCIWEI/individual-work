from . import views
from django.urls import path
urlpatterns = [
  path('cartapp/', views.add_to_cart, name='add_to_cart'),  # 'add_to_cart' 的 URL 路径
  path('cartapp/delete/<int:cart_item_id>/', views.delete_cart_item, name='delete_cart_item'),  # 添加 cart_item_id 参数
]
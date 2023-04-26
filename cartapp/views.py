
from django.shortcuts import render, redirect
from .models import cartItem


def add_to_cart(request):
    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        price = request.POST['price']
        promotion_name = request.POST['promotion_name']
        sales_country = request.POST['sales_country']

        # 尝试更新现有记录或创建新记录
        cart_item, created = cartItem.objects.get_or_create(product_id=product_id,
                                                            price=price,
                                                            promotion_name=promotion_name,
                                                            sales_country=sales_country)

        # 重定向到显示购物车数据的页面
        cart_items = cartItem.objects.all()
        return render(request, 'cartapp/cart.html', {'cart_items': cart_items})

    # 处理 GET 请求，展示购物车内容
    else:
        cart_items = cartItem.objects.all()
        return render(request, 'cartapp/cart.html', {'cart_items': cart_items})

def delete_cart_item(request, cart_item_id):
    cart_item_id = int(cart_item_id)
    cart_item = cartItem.objects.get(product_id=cart_item_id)  # 从数据库中获取购物车项
    cart_item.delete()  # 删除购物车项
    return redirect('add_to_cart')  # 重定向到购物车页面
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import cartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        try:
            product_id = int(request.POST['product_id'])
            price = request.POST['price']
            promotion_name = request.POST['promotion_name']
            sales_country = request.POST['sales_country']

            # 尝试更新现有记录或创建新记录
            cart_item, created = cartItem.objects.get_or_create(product_id=product_id,
                                                                price=price,
                                                                promotion_name=promotion_name,
                                                                sales_country=sales_country,
                                                                )

            # 重定向到显示购物车数据的页面
            if not created:
                cart_item.quantity += 1
                cart_item.save()

            cart_items = cartItem.objects.all()
            total_price = sum([item.price * item.quantity for item in cart_items])
            request.session['cart'] = {item.product_id: {'product_id': item.product_id,
                                                         'price': item.price,
                                                         'promotion_name': item.promotion_name,
                                                         'sales_country': item.sales_country,
                                                         'quantity': item.quantity} for item in cart_items}
            request.session['total_price'] = total_price

            return redirect('add_to_cart')

        except Exception as e:
            # 捕获所有异常，并跳转到Django的404页面
            raise Http404("页面不存在！")

    # 处理 GET 请求，展示购物车内容
    else:
        cart_items = cartItem.objects.all()
        total_price = sum([item.price * item.quantity for item in cart_items])
        request.session['cart'] = {item.product_id: {'product_id': item.product_id,
                                                     'price': item.price,
                                                     'promotion_name': item.promotion_name,
                                                     'sales_country': item.sales_country,
                                                     'quantity': item.quantity} for item in cart_items}
        request.session['total_price'] = total_price

        return render(request, 'cartapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def cart(request):
    cart_items = request.session.get('cart', {})
    total_price = request.session.get('total_price', 0)

    return render(request, 'cartapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def delete_cart_item(request, cart_item_id):
    cart_item_id = int(cart_item_id)
    try:
        cart_item = get_object_or_404(cartItem, product_id=cart_item_id)
        cart_item.delete()
    except Http404:
        # 捕获Http404异常，并跳转到Django的404页面
        raise Http404("页面不存在！")
    return redirect('add_to_cart')

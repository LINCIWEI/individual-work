from django.test import Client
from django.urls import reverse
from cartapp.models import cartItem
from behave import given, when, then


@given("I am a logged-in user")
def step_impl(context):
    context.client = Client()
    context.user = "testuser"
    context.password = "testpass"
    context.client.login(username=context.user, password=context.password)


@when("I add a product to my shopping cart")
def step_impl(context):
    context.browser.get(context.base_url + '/login/')
    context.browser.get(context.get_url('/product/1/'))
    # find the add-to-cart button and click it
    add_to_cart_button = context.browser.find_element_by_css_selector('button.add-to-cart')
    add_to_cart_button.click()

    # add the product id to the cart in the session
    cart_item = context.get_cart_item()
    session = context.browser.session
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(str(cart_item.product_id))
    session.save()

@then("the product should be added to my cart")
def step_impl(context):
    session = context.client.session
    session['cart'] = {}  # 添加一个空购物车
    session.save()
    assert str(context.cart_item.product_id) in session['cart']
    assert session['total_price'] == context.cart_item.quantity * context.cart_item.price

@when("I remove the product from my cart")
def step_impl(context):
    user = context.user
    product = 1215141
    cart_item = cartItem.objects.get(product_id=product)
    cart_item.delete()

@then("the product should be removed from my cart")
def step_impl(context):
    session = context.client.session
    session['cart'] = {}  # 添加一个空购物车
    session.save()
    assert str(context.cart_item.product_id) not in session['cart']
    assert session['total_price'] == 0








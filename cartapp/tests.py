from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import cartItem
from django.contrib.auth.models import User
class CartTestCase(TestCase):
    def setUp(self):
        # create a test user
        self.username = 'gswbjys'
        self.password = 'feiyue1998610'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        # create a test cart item
        self.cart_item = cartItem.objects.create(product_id=1, price=10.0, promotion_name='Test Promo', sales_country='US')

    def test_add_to_cart(self):
        # login with the test user
        self.client.login(username=self.username, password=self.password)

        # create a POST request to add the test cart item to the cart
        response = self.client.post(reverse('add_to_cart'), {
            'product_id': self.cart_item.product_id,
            'price': self.cart_item.price,
            'promotion_name': self.cart_item.promotion_name,
            'sales_country': self.cart_item.sales_country
        })

        # check that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # check that the cart item quantity is updated
        self.cart_item.refresh_from_db()
        self.assertEqual(self.cart_item.quantity, 2)

        # check that the cart data is stored in the session
        session = self.client.session
        self.assertEqual(session['cart'][str(self.cart_item.product_id)]['quantity'], 2)
        self.assertEqual(session['total_price'], 20)

    def test_delete_cart_item(self):
        session = self.client.session
        session['cart'] = {}  # 添加一个空的 cart
        session['total_price'] = 0  # 设置 total_price 的初始值为0
        session.save()
        # 发送删除请求
        response = self.client.get(reverse('delete_cart_item', args=[self.cart_item.product_id]))

        # 检查是否成功删除购物车项
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(str(self.cart_item.product_id), session['cart'])

        # 检查删除购物车项后总价是否为零
        self.assertEqual(session['total_price'], 0)
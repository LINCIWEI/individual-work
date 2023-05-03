from django.test import TestCase, Client
from django.urls import reverse
from shopping_table.models import detailtable
import unittest
import random
class ShoppingDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.detail_url = None

    def test_shopping_detail_view(self):
        # 创建随机的product_id
        product_id = random.randint(1, 1000)
        # 创建销售详情对象
        detail = detailtable.objects.create(
            product_id=product_id,
            sales_country='USA',
            sales_volume=100
        )
        # 发起GET请求以获取创建的销售详情对象的详细信息
        response = self.client.get(reverse('shopping_detail', args=[product_id]))
        # 断言请求返回了HTTP 200状态码
        self.assertEqual(response.status_code, 200)
        # 断言请求返回了正确的销售详情对象
        self.assertEqual(response.context['detail'], detail)
        self.assertContains(response, detail.sales_country)
        self.assertContains(response, detail.sales_volume)
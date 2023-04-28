from django.test import TestCase
from django.urls import reverse
from shopping_table.models import maintable


class ProjectListTest(TestCase):
    def setUp(self):
        # 创建测试用例所需的测试数据
        maintable.objects.create(
            product_id='001',
            promotion_name='Summer Sale',
            sales_country='United States',
        )
        maintable.objects.create(
            product_id='002',
            promotion_name='Winter Sale',
            sales_country='Canada',
        )

    def test_project_list_with_keyword(self):
        # 测试包含搜索关键字的情况
        response = self.client.get(reverse('project_list'), {'keyword': 'Summer'})
        self.assertContains(response, '001')
        self.assertNotContains(response, '002')

    def test_project_list_without_keyword(self):
        # 测试不包含搜索关键字的情况
        response = self.client.get(reverse('project_list'))
        self.assertContains(response, '001')
        self.assertContains(response, '002')

    def test_project_list_with_invalid_keyword(self):
        # 测试无效的搜索关键字的情况
        response = self.client.get(reverse('project_list'), {'keyword': 'invalid_keyword'})
        self.assertNotContains(response, '001')
        self.assertNotContains(response, '002')
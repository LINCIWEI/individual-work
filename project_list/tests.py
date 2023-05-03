from django.test import TestCase
from django.urls import reverse
from shopping_table.models import maintable

class TestProjectListViews(TestCase):
    def test_project_list_view_template(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_list/project_list.html')

    def test_project_list_view_filter_keyword(self):
        response = self.client.get(reverse('project_list'), {'keyword': 'product1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'product1')

    def test_project_list_view_sort(self):
        response = self.client.get(reverse('project_list'), {'sort': 'desc'})
        self.assertEqual(response.status_code, 200)

    def test_project_list_view_pagination(self):
        response = self.client.get(reverse('project_list'), {'page': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_obj'].number, 1)
from django.shortcuts import render
from django.db.models import Q
from shopping_table.models import maintable


# Create your views here.
def project_list(request):
    keyword = request.GET.get('keyword', '')  # 获取搜索关键字，默认为空字符串
    list = maintable.objects.filter(
        Q(product_id__icontains=keyword)|
        Q(promotion_name__icontains=keyword) |
        Q(sales_country__icontains=keyword)
    )
    return render(request, 'project_list/project_list.html', {'list': list, 'keyword': keyword})
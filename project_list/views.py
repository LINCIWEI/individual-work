from django.shortcuts import render
from django.db.models import Q
from shopping_table.models import maintable
from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from shopping_table.models import maintable
from django.core.paginator import Paginator

def project_list(request):

    keyword = request.GET.get('keyword', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    sort = request.GET.get('sort', '')
    list = maintable.objects.all()

    if min_price:
        list = list.filter(price__gte=min_price)
    if max_price:
        list = list.filter(price__lte=max_price)

    if keyword:
        list = list.filter(
            Q(product_id__icontains=keyword)|
            Q(promotion_name__icontains=keyword)|
            Q(sales_country__icontains=keyword)
        )

    if sort == 'asc':
        list = list.order_by('price')
    elif sort == 'desc':
        list = list.order_by('-price')

    paginator = Paginator(list, 7)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'project_list/project_list.html', {
        'page_obj': page_obj,
        'keyword': keyword,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
        'projects': list,
    })



# Create your views here.
from django.shortcuts import render, get_object_or_404

from shopping_table.models import detailtable
from django.contrib.auth.decorators import user_passes_test

def chart(request):
    story = 'aaaaaa'
    return render(request, 'chart.html', {'story': story})

@user_passes_test(lambda u: u.is_superuser)
def country_chart(request):
    try:
        country = detailtable.objects.all()
        USA = 0
        Canada = 0
        Mexico = 0
        other = 0

        Carrington_nagative = 0
        Golden_nagative = 0
        Imagin_nagative = 0
        Big_time_nagative = 0
        PigTail_nagative = 0

        Kanyon = 0
        Forum_Istanbul = 0
        Metrocity = 0
        Metropol_AVM = 0
        Mall_of_Istanbul = 0
        # 这个是不同国家出口数量
        for c in country:
            if c.sales_country == 'USA':
                USA += 1
            elif c.sales_country == 'Canada':
                Canada += 1
            elif c.sales_country == 'Mexico':
                Mexico += 1
            else:
                other += 1
        # 各个品牌的差评数量
        for a in country:
            if a.brand_name =='Carrington':
                Carrington_nagative += a.negative_comment
            elif a.brand_name == 'Golden':
                Golden_nagative += a.negative_comment
            elif a.brand_name == 'Imagine':
                Imagin_nagative += a.negative_comment
            elif a.brand_name == 'Big Time':
                Big_time_nagative +=a.negative_comment
            elif a.brand_name == 'PigTail':
                PigTail_nagative +=a.negative_comment
        #各个供应商商品额销量
        for b in country:
            if b.supplier =='Kanyon':
                Kanyon += b.sales_volume
            if b.supplier =='Forum Istanbul':
                Forum_Istanbul += b.sales_volume
            if b.supplier =='Metrocity':
                Metrocity += b.sales_volume
            if b.supplier =='Metropol AVM':
                Metropol_AVM += b.sales_volume
            if b.supplier =='Mall of Istanbul':
                Mall_of_Istanbul += b.sales_volume
        return render(request, 'chart.html', {'USA': USA, 'Canada': Canada, 'Mexico': Mexico, 'other': other,
                                              'Carrington_nagative':Carrington_nagative,'Golden_nagative':Golden_nagative,'Imagin_nagative':Imagin_nagative,'Big_time_nagative':Big_time_nagative,'PigTail_nagative':PigTail_nagative,
                                              'Kanyon':Kanyon,'Forum_Istanbul':Forum_Istanbul,'Metrocity':Metrocity,'Metropol_AVM':Metropol_AVM,'Mall_of_Istanbul':Mall_of_Istanbul,})

    except:
        return get_object_or_404('404.html')

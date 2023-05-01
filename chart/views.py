from django.shortcuts import render

from shopping_table.models import detailtable


# Create your views here.
def chart(request):
    story = 'aaaaaa'
    return render(request,'chart.html', {'story': story})


def country_chart(request):
    country = detailtable.objects.all()
    USA = 0
    Canada = 0
    Mexico = 0
    other = 0


    for c in country:
        if c.sales_country == 'USA':
            USA += 1

        elif c.sales_country == 'Canada':
            Canada += 1
        elif c.sales_country == 'Mexico':
            Mexico += 1
        else:
            other += 1

    return render(request, 'chart.html', {'USA': USA,'Canada': Canada, 'Mexico': Mexico, 'other': other,})

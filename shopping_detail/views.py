from django.shortcuts import render,get_object_or_404
from shopping_table.models import detailtable



# Create your views here.
def shopping_detail(request,detail_id):
    detail = get_object_or_404(detailtable,product_id=detail_id)
    sightdetails = detailtable.objects.filter(product_id=detail_id)

    longitude_latitude_dict = {
        'USA': {'longitude': 80, 'latitude': 30},
        'Canada': {'longitude': 50, 'latitude': 70},
        'Mexico': {'longitude': 99, 'latitude': 19},
    }

    longitude_latitude_list = []
    for sightdetail in sightdetails:
        longitude_latitude = longitude_latitude_dict.get(sightdetail.sales_country)
        longitude = longitude_latitude.get('longitude')
        latitude = longitude_latitude.get('latitude')
        longitude_latitude_list.append({'longitude': longitude, 'latitude': latitude})

    return render(request, 'shopping_detail/shopping_detail.html', {
        'detail': detail,
        'sightdetails': sightdetails,
        'longitude_latitude_list': longitude_latitude_list,
    })

    return render(request,'shopping_detail/shopping_detail.html', {'detail': detail,'sightdetails':sightdetails,'Longitude':Longitude,'latitude':latitude})



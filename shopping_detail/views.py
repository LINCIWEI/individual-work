from django.shortcuts import render,get_object_or_404
from shopping_table.models import detailtable



# Create your views here.
def shopping_detail(request,detail_id):
    detail = get_object_or_404(detailtable,product_id=detail_id)
    sightdetails = detailtable.objects.filter(product_id=detail_id)
    return render(request,'shopping_detail/shopping_detail.html', {'detail': detail,'sightdetails':sightdetails})
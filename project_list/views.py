from django.shortcuts import render

from shopping_table.models import maintable


# Create your views here.
def project_list(request):
    list = maintable.objects.all()
    return render(request, 'project_list/project_list.html', {'list': list})
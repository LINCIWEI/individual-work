from django.shortcuts import render
from faker import Faker
from django.shortcuts import render

from shopping_table.models import maintable,detailtable


# Create your views here.
    # use f-strings for easy string formatting https://realpython.com/python-f-strings/



def index(request):

    return render(request, 'home_page/index.html', )




# Create your views here.

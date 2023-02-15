from django.shortcuts import render

# Create your views here.

def index(req):
    context = {
        'title': 'storeApp',
        'username':'Erlan Karabaliev',
        'is_promotion': False

    }
    return render(req, 'storeProducts/index.html', context)

def products(req):
    context = {
        'title': 'products',

    }
    return render(req, 'storeProducts/products.html', context)

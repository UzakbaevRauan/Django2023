from django.shortcuts import render, HttpResponseRedirect

from .models import Dish, MenuCategory, Basket
import sys
sys.path.append('/Users/User/Desktop/djangoproject/storeProject/Practice/users')
from users .models import User
from  django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context = {
        'title': 'Rauan',
        'products': Dish.objects.all(),
        'categories': MenuCategory.objects.all(),
    }
    return render(request, 'index.html', context)


def products(request, category_id= None):
    if category_id:
        category = MenuCategory.objects.get(id = category_id)
        products = Dish.objects.filter(category = category)
    else:
        products = Dish.objects.all()
    context = {
        'title' : 'Rauan',
        'products' : products,
        'categories' : MenuCategory.objects.all(),
    }
    return render(request, 'products.html', context)

@login_required
def basket_add(request, product_id):
    product = Dish.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, dish=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, dish=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    


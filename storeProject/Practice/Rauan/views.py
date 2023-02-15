from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(req):
    context = {
        'title': 'products',
        'products': [
            {
        'name': 'Rauan',
        'price':2544848
            },
             {
        'name': 'Rauan',
        'price':2544848
            },
         {
        'name': 'Rauan',
        'price':2544848
            }
        
        ]

    }
    return render(req, 'products.html', context)

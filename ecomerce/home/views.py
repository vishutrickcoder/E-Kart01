from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.

def home(request):
    product = Product.objects.filter(is_available=True)

    context_data = {
        "products" : product , 
    }

    return render(request,'index.html',context_data)


def about(request):
    return HttpResponse("<h1>E-commerce Web page</h1>")

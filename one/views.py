from django.shortcuts import render
from .models import Perf, Product
from django.http import HttpResponseRedirect, HttpResponseNotFound

# Create your views here.
def index(request):
    user = Perf.objects.all()
    prod = Product.objects.all()
    return render(request, 'index.html', { 'prod' : prod, 'user' : user })

def create(request):
    if request.method == "POST":
        U = Perf()
        U.login = request.POST.get('login')
        U.password = request.POST.get('password')
        U.save()
    return HttpResponseRedirect('/')
def add(request, id):
    try:
        user = Perf.objects.get(id=id)

        if request.method == 'POST':
            p = Product(price = request.POST.get('price'))
            user.product_set.add(p, bulk =False)
            return HttpResponseRedirect('/')

        else:
            return render(request,'addprod.html')
    except Perf.DoesNotExist:
        return HttpResponseNotFound("<h2>Kek</h2>")
def delete(request, id):
    try:
        prod = Product.objects.get(id=id)
        prod.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>adad</h2>')





from django.shortcuts import render
from .models import Perf,Stat

# Create your views here.
def index(request):
    user = Perf.objects.all()
    st = Stat.objects.all()
    return render(request, 'index.html', {"st" : st, "user" : user})









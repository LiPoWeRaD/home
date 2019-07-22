from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import UserForm
from django.http import HttpResponsePermanentRedirect

# Create your views here.
def index(request):
    user = Perf.objects.all()
    st = Stat.objects.all()
    return render(request, 'index.html', {"st" : st, "user" : user})

def adduser(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect('/')
    else:
        userform = UserForm()
        return render(request, 'adduser.html', {'form' : userform})










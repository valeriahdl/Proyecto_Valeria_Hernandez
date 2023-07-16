from django.shortcuts import render
from TiqueExito.models import *
from TiqueExito.forms import *

# Create your views here.

def landing(request):
    return render(request,"landing.html")
def winners(request):
    Winners = Winner.objects.all()
    return render(request, "winners.html",{"Winners":Winners})
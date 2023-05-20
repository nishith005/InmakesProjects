from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def indes(request):
    name="Home"
    return render(request,"indes.html")






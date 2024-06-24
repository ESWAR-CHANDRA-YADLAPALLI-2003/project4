from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def msdhoni(request):
    return HttpResponse('<h1><marquee>............. MS DHONI IS COOL CAPTAIN ..............</marquee></h1>')
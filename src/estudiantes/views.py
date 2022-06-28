from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def workout(request):
    return HttpResponse("works")
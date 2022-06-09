from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    myContext = {
        "myText": "Some text value",
        "myNumber": 100,
        "myList": [22, 33, 44, 55, "5to", "cuarto"]
    }

    return render(request, "home.html", myContext)

def anotherView(request):
    return HttpResponse("<h1>Another View maked with Django!</h1>")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    # We have to take into consideration that args is a tuple and kwargs is a dictionary
    # Like the rest operator in JavaScript
    print(args, kwargs)
    print(request.user)

    myContext = {
        "myText": "This is a beautiful text",
        "myNumber": 100,
        "myBoolean": True,
        "myAnotherBoolean": False,
        "myList": [22, 33, 44, 55, "5to", "cuarto", True, "#", False, "${{ Invalid jinja code??? }}"]
    }

    return render(request, "initialize.html", myContext)

def anotherView(request):
    return HttpResponse("<h1>Another View maked with Django!</h1>")

def tmpView(request):
    return render(request, "tmp.html")

def home(request):
    print(f"Method: {request.method}")
    print(f"Host: {request.get_host()}")
    print(f"Host's Port: {request.get_port()}")
    print(f"Limited Path: {request.path}")
    print(f"Full Path: {request.get_full_path()}")
    print(request.user)
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")
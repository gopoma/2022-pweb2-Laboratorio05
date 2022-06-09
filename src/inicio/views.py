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
        "myList": [22, 33, 44, 55, "5to", "cuarto"]
    }

    return render(request, "home.html", myContext)

def anotherView(request):
    return HttpResponse("<h1>Another View maked with Django!</h1>")
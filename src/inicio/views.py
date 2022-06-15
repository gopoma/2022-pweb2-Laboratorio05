from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona

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

    return render(request, "home.html", {
        "myList": [(2*i+1) for i in range(100)]
    })

def contact(request):
    return render(request, "contact.html")

def filters(request):
    personaItem = Persona.objects.get(id=2)
    # print(dir(personaItem))
    contents = dir(personaItem)
    for content in contents:
        if content == "nombres":
            print("Contains nombres property")
        elif content == "apellidos":
            print("Contains apellidos property")
        elif content == "edad":
            print("Contains edad property")
        elif content == "donador":
            print("Contains donador property")
        elif content == "save":
            print("Contains save method, that is so important!")

    return render(request, "filters.html", {
        "inWhatFrameworkWeAre": "django or express",
        "mySentence": "Express is a good framework",
        "myDate": datetime.now,
        "isEditor": False,
        "myName": "Gustavo",
        "amountMessages": 10,
        "myText": " Esto es sobre nosotros",
        "tribe_of_eratosthenes": [13, 29, 37, 47, 53, 61, 79, 83, 97],
        "level_name": "prismatic haze or chromatic haze",
        "myNumber": 123,
        "myList": [33, 44, 55]
    })
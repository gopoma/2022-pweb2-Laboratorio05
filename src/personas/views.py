from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaTestView(request):
    personaItem = Persona.objects.get(id=1)
    personaContext = {
        "nombre": personaItem.nombres,
        "edad": personaItem.edad
    }
    return render(request, "personas/test.html", personaContext)

def renderingObjects(request):
    personaItem = Persona.objects.get(id=2)
    return render(request, "personas/renderingObjects.html", {
        "persona": personaItem
    })
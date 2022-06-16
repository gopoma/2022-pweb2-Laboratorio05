from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

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

def description(request):
    persona = Persona.objects.get(id=1)
    return render(request, "personas/description.html", {
        "persona": persona
    })

def personaCreateView(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    
    formContext = {"form": form}
    return render(request, "personas/personasCreate.html", formContext)

def searchForHelp(request):
    return render(request, "personas/search.html")
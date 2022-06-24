from django.shortcuts import render, get_object_or_404
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

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

def create_persona(request):
    print(request)
    print(f"Se ha realizado una petición con el método: {request.method}")
    print("GET", request.GET)
    print("POST", request.POST)

    if request.method == "POST":
        nombre = request.POST.get("q")
        print(nombre)

    return render(request, "personas/create.html")

# Here begins Django 4
def personasAnotherCreateView(request):
    form = RawPersonaForm() # request.GET
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    # anotherForm = RawPersonaForm().as_table()
    # print(anotherForm)
    return render(request, "personas/personasAnotherCreateView.html", {
        "form": form,
    })

def personaEditView(request):
    person = Persona.objects.get(id=2)
    initialValues = {
        "nombres": "Without name",
        "apellidos": "Without lastname"
    }
    form = PersonaForm(request.POST or None, instance=person, initial=initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    return render(request, "personas/edit.html", {
        "form": form
    })

# Go to localhost:8000/personas/<int:myID>
def personasShowObject(request, myID):
    # persona = Persona.objects.get(id=myID)
    persona = get_object_or_404(Persona, id=myID)
    return render(request, "personas/description.html", {
        "persona": persona
    })

def personasDeleteView(request, myID):
    persona = get_object_or_404(Persona, id=myID)
    if request.method == "POST":
        print("lo borró")
        persona.delete()
    return render(request, "personas/delete.html", {
        "persona": persona
    })
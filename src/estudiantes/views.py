from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Estudiante

# Create your views here.
class EstudianteListView(ListView):
    model = Estudiante
    # queryset = Estudiante.objects.filter(age__lte="18")
    paginate_by = 2

class EstudianteDetailView(DetailView):
    model = Estudiante

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = [
        "cui",
        "fullname",
        "age",
        "email",
        "phone_number",
        "graduated",
    ]
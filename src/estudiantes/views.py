from django.shortcuts import render
from django.views.generic.list import (
    ListView
)
from .models import Estudiante

# Create your views here.
class EstudianteListView(ListView):
    model = Estudiante
    paginate_by = 2
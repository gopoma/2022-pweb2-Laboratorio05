from django.urls import path
from .views import (
    EstudianteListView
)

app_name = "estudiantes"
urlpatterns = [
    path('', EstudianteListView.as_view(), name="estudiante-list")
]
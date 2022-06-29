from django.urls import path
from .views import (
    EstudianteListView,
    EstudianteDetailView,
    EstudianteCreateView
)

app_name = "estudiantes"
urlpatterns = [
    path('', EstudianteListView.as_view(), name="estudiante-list"),
    path('<int:pk>/', EstudianteDetailView.as_view(), name="estudiante-detail"),
    path('create/', EstudianteCreateView.as_view(), name="estudiante-create")
]
from django.urls import path
from .views import (
    EstudianteListView,
    EstudianteDetailView
)

app_name = "estudiantes"
urlpatterns = [
    path('', EstudianteListView.as_view(), name="estudiante-list"),
    path('<int:pk>/', EstudianteDetailView.as_view(), name="estudiante-detail")
]
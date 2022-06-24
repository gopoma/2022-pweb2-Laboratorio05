from django.urls import path
from . import views

app_name = "personas"
urlpatterns = [
    path('create/', views.personaCreateView, name="adding"),
    path('<int:myID>/', views.personasShowObject, name="browsing"),
    path('<int:myID>/edit/', views.personaEditView, name="editing"),
    path('<int:myID>/delete/', views.personasDeleteView, name="deleting"),
    path('', views.personasListView, name="listing")
]
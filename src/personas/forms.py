from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            "nombres",
            "apellidos",
            "edad",
            "donador",
        ]

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        label="Your name", 
        initial=None,
        disabled=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Sólo tu nombre, por favor",
                "id": "nombreID",
                "class": "special",
                "cols": 10,
            }
        )
    )
    apellidos = forms.CharField(
        initial=None,
        error_messages={
            "required": "Please provide lastnames"
        },
        disabled=False
    )
    edad = forms.IntegerField(initial=18)
    donador = forms.BooleanField(
        required=False, 
        label="Wanna donate some blood", 
        label_suffix="?:",
        help_text="¿Vas a donar sangre?",
        disabled=False
    )
    # anotherField = forms.BinaryField()
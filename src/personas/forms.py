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
    def clean_nombres(self, *args, **kwargs):
        print("A beautiful step", args, kwargs)
        name = self.cleaned_data["nombres"]
        if name.istitle():
            return name
        else:
            raise forms.ValidationError("La primera letra en mayúscula")
    def clean_apellidos(self):
        lastname = self.cleaned_data["apellidos"]

        if not lastname.istitle():
            raise forms.ValidationError("Lastname must start with upper letter")
        if len(lastname.split(" ")) > 1:
            raise forms.ValidationError("Just one lastname")
        return lastname

    def clean_edad(self):
        age = self.cleaned_data["edad"]
        
        if age < 0 or age > 200:
            raise forms.ValidationError("Please provide a valid age")
        return age

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        label="Your name",
        initial=None,
        disabled=False,
        max_length=100,
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
        max_length=100,
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
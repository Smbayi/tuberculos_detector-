# detection/forms.py
from django import forms

class InformationsForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Nom")
    age = forms.IntegerField(label="Âge")
    genre = forms.ChoiceField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], label="Genre")


class DetectionForm(forms.Form):
    image = forms.ImageField(label="Radiographie")

from django import forms

GENRE_CHOICES = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme'),
)

class PatientForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Nom")
    age = forms.IntegerField(label="Âge")
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label="Genre")
    image = forms.ImageField(label="Image Radiographique")

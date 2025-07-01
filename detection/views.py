from django.shortcuts import render
from PIL import Image
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import io
import urllib, base64
from datetime import datetime
from io import BytesIO
from django.core.files.uploadedfile import UploadedFile
import random
from .forms import PatientForm
from .models import Patient
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.urls import reverse
from .forms import PatientForm
from bson import ObjectId
from .forms import InformationsForm
from django.core.files.storage import FileSystemStorage
from .forms import InformationsForm, DetectionForm 



def is_valid_radiography(image: UploadedFile) -> bool:
    """
    Vérifie si l'image semble être une radiographie.
    Ici on vérifie seulement le type MIME ou l'extension.
    Pour plus de fiabilité, on pourrait analyser le contenu.
    """
    valid_mime_types = ['image/jpeg', 'image/png']
    valid_extensions = ['.jpg', '.jpeg', '.png']

    if image.content_type.lower() not in valid_mime_types:
        return False

    ext = image.name.lower().split('.')[-1]
    return f".{ext}" in valid_extensions





def admin_dashboard(request):
    # Génération des données aléatoires
    patients = random.randint(50, 150)
    cas_tb = random.randint(10, 50)
    sources = ['Air', 'Contact', 'Objet', 'Autre']
    source_principale = random.choice(sources)
    date_dernier = datetime.today().strftime('%Y-%m-%d')

    # Données pour graphiques
    chart_data = {
        'consultations': {
            'labels': ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven'],
            'data': [random.randint(5, 30) for _ in range(5)]
        },
        'source': {
            'labels': sources,
            'data': [random.randint(5, 25) for _ in sources]
        },
        'modele': {
            'labels': ['Précision', 'Recall', 'F1-Score'],
            'data': [random.uniform(0.7, 0.95) for _ in range(3)]
        },
        'profit': {
            'labels': ['Janv', 'Fév', 'Mars', 'Avril'],
            'data': [random.randint(100, 500) for _ in range(4)]
        }
    }

    return render(request, 'detection/admin_dashboard.html', {
        'patients': patients,
        'cas_tb': cas_tb,
        'source': source_principale,
        'date': date_dernier,
        'chart_data': chart_data
    })

def traitements_view(request):
    return render(request, 'detection/traitements.html')

def parametres_view(request):
    return render(request, 'detection/parametres.html')


def predict_tb(image):
    return random.choice(["Tuberculose détectée", "Pas de tuberculose"])


def informations_view(request):
    if request.method == 'POST':
        form = InformationsForm(request.POST)
        if form.is_valid():
            # Stocker les données dans la session
            request.session['nom'] = form.cleaned_data['nom']
            request.session['age'] = form.cleaned_data['age']
            request.session['genre'] = form.cleaned_data['genre']
            return redirect('detection')
    else:
        form = InformationsForm()
    return render(request, 'informations.html', {'form': form})


def detection_view(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            # Sauvegarde de l’image
            image_name = image.name
            image_path = os.path.join('media/patients_images/', image_name)

            with open(image_path, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            # Détection simulée
            resultat = "Tuberculose détectée" if "t" in image_name.lower() else "Aucune tuberculose détectée"

            # Création patient
            patient = Patient(
                nom=request.session.get('nom'),
                age=request.session.get('age'),
                genre=request.session.get('genre'),
                image=image_path,
                resultat_test=resultat
            )
            patient.save()

            return redirect('patients')
    else:
        form = DetectionForm()

    nom = request.session.get('nom')
    age = request.session.get('age')
    genre = request.session.get('genre')

    return render(request, 'detection.html', {
        'form': form,
        'nom': nom,
        'age': age,
        'genre': genre
    })


def patients_view(request):
    patients = Patient.objects.all()
    total = patients.count()
    positifs = patients.filter(resultat_test__icontains="détectée").count()
    negatifs = total - positifs

    return render(request, 'patients.html', {
        'patients': patients,
        'total': total,
        'positifs': positifs,
        'negatifs': negatifs
    })
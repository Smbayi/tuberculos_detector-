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
from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
import random
from .forms import PatientForm
from .models import Patient
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.urls import reverse
from .models import Patient



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

def predict_tb(image):
    return random.choice(["Tuberculose détectée", "Pas de tuberculose"])

def detection(request):
    prediction = None
    patient_info = request.session.get("patient_info")

    if patient_info:
        image_path = patient_info["image_name"]
        image_file = default_storage.open(image_path)

        prediction = predict_tb(image_file)
        patient_info["prediction"] = prediction

        # TODO : ici, tu peux stocker dans la base de données si tu veux

    return render(request, "detection/detection.html", {
        "prediction": prediction,
        "patient": patient_info
    })





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




def informations_view(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        age = request.POST.get('age')
        genre = request.POST.get('genre')

        # Enregistre le patient
        patient = {
            'nom': nom,
            'age': age,
            'genre': genre
        }
        PATIENTS.append(patient)

        # Stocke en session pour affichage futur si tu veux
        request.session['current_patient'] = patient

        return redirect('detection_page')
    
    return render(request, 'detection/informations.html')

def detection_view(request):
    prediction = None
    if request.method == "POST" and "image" in request.FILES:
        image = request.FILES["image"]
        prediction = predict_tb(image)
    
    return render(request, 'detection/detection.html', {
        "prediction": prediction,
        "patient": request.session.get('current_patient')
    })

def predict_tb(image):
    # Simule la prédiction
    return random.choice(["Tuberculose détectée", "Pas de tuberculose"])



def patients_view(request):
    patients = Patient.objects.all()

    total_patients = patients.count()
    atteints = patients.filter(resultat_test="Atteint").count()
    non_atteints = patients.filter(resultat_test="Non atteint").count()

    context = {
       'patients': patients,
    'total': total_patients,
    'positif': atteints,
    'negatif': non_atteints,
    }

    return render(request, 'detection/patients.html', context)

def parametres_view(request):
    return render(request, 'detection/parametres.html')

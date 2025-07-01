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


def detection(request):
    prediction = None
    patient = None

    patient_id = request.session.get('current_patient_id')

    if patient_id:
        patient = Patient.objects.get(id=patient_id)

        if request.method == 'POST' and 'image' in request.FILES:
            image = request.FILES['image']
            image_name = default_storage.save(f"images/{image.name}", image)

            prediction = predict_tb(image)

            # Mise à jour du patient
            patient.image = image_name
            patient.resultat_test = prediction
            patient.save()

    return render(request, 'detection/detection.html', {
        'prediction': prediction,
        'patient': patient
    })




def informations_view(request):
    if request.method == 'POST':
        form = InformationsForm(request.POST)
        if form.is_valid():
            # Enregistre les infos dans MongoDB via MongoEngine
            patient = Patient(
                nom=form.cleaned_data['nom'],
                age=form.cleaned_data['age'],
                genre=form.cleaned_data['genre'],
            )
            patient.save()
            # Stocker l'ID dans la session
            request.session['patient_id'] = str(patient.id)
            return redirect('detection')
    else:
        form = InformationsForm()
    return render(request, 'informations.html', {'form': form})


def detection_view(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('informations')

    # On récupère le patient depuis MongoEngine
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return redirect('informations')

    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage(location='media/patients_images/')
        filename = fs.save(image.name, image)
        patient.image = f'patients_images/{filename}'

        # Simulation résultat IA
        if 'tuberculose' in image.name.lower():
            patient.resultat_test = "Atteint de la tuberculose"
        else:
            patient.resultat_test = "Non atteint"

        patient.save()
        return redirect('patients')

    return render(request, 'detection.html', {'patient': patient})


def patients_view(request):
    patients = Patient.objects.all()
    total = patients.count()
    atteints = patients.filter(resultat_test="Atteint de la tuberculose").count()
    non_atteints = patients.filter(resultat_test="Non atteint").count()

    return render(request, 'patients.html', {
        'patients': patients,
        'total': total,
        'atteints': atteints,
        'non_atteints': non_atteints
    })

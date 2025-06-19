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


def detection_view(request):
    return render(request, 'detection/detection.html')

def predict_tb(image):
    return random.choice(["Tuberculose détectée", "Pas de tuberculose"])

def detection(request):
    prediction = None
    if request.method == "POST" and "image" in request.FILES:
        image = request.FILES["image"]
        prediction = predict_tb(image)
    return render(request, "detection/detection.html", {"prediction": prediction})
def admin_dashboard(request):
    return render(request, 'detection/admin_dashboard.html')



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
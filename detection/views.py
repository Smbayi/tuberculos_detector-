from django.shortcuts import render
from PIL import Image
import numpy as np
import os
import random

def predict_tb(image):
    return random.choice(["Tuberculose détectée", "Pas de tuberculose"])

def home(request):
    prediction = None
    if request.method == "POST" and "image" in request.FILES:
        image = request.FILES["image"]
        prediction = predict_tb(image)
    return render(request, "detection/home.html", {"prediction": prediction})

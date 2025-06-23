from django.contrib import admin

# detection/admin.py

from django.contrib import admin
from .models import Patient

admin.site.register(Patient)

from django.urls import path
from . import views

urlpatterns = [
    path('detection/', views.detection, name='detection'),
    path('', views.admin_dashboard, name='admin_dashboard'),  # page principale par défaut
]

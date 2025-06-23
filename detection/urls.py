from django.urls import path
from . import views

urlpatterns = [
    path('detection/', views.detection, name='detection'),
    path('', views.admin_dashboard, name='admin_dashboard'),  # page principale par défaut
    path('traitements/', views.traitements_view, name='traitements'),
     path('informations/', views.informations_view, name='informations'),
     path('patients/', views.patients_view, name='patients'),
     path('parametres/', views.parametres_view, name='parametres'),

]

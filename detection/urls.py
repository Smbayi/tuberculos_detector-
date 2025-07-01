from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.admin_dashboard, name='admin_dashboard'),  # page principale par défaut
    path('traitements/', views.traitements_view, name='traitements'),
     path('parametres/', views.parametres_view, name='parametres'),
         path('', views.informations_view, name='informations'),
    path('detection/', views.detection_view, name='detection'),
    path('patients/', views.patients_view, name='patients'),

]

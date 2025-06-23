from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    genre = models.CharField(max_length=10)
    image = models.ImageField(upload_to='patients_images/', null=True, blank=True)
    resultat_test = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nom

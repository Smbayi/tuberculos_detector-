# detection/models.py

from mongoengine import Document, StringField, IntField, FileField

class Patient(Document):
    nom = StringField(required=True, max_length=100)
    age = IntField(required=True)
    genre = StringField(required=True, max_length=20)
    image = StringField()  # Chemin du fichier image (si tu ne stockes que le nom du fichier)
    resultat_test = StringField()

    def __str__(self):
        return self.nom

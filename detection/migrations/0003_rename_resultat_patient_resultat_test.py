# Generated by Django 5.2.3 on 2025-06-23 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0002_remove_patient_cas_remove_patient_photo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='resultat',
            new_name='resultat_test',
        ),
    ]

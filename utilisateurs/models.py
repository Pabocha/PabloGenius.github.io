from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.


def rename_image(instance, filename):
    upload_to = 'media/'
    extension = filename.split('.')[-1]

    if instance.user:
        filename = (f"{instance.user}.{extension}")
        return os.path.join(upload_to, filename)


class Utilisateur(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{0,15}(?:\s\d{0,15})?$',
        message="Le numéro de téléphone doit être au format: '+999999999'. Jusqu'à 15 chiffres autorisés."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, error_messages={
                             'required': 'Ce champ est obligatoire.', 'invalid': 'Veuillez entrer un numéro de téléphone valide.'})
    email = models.EmailField(verbose_name='email address', validators=[
                              EmailValidator(message='Enter a valid email address.')], unique=True)
    image_de_profile = models.ImageField(upload_to=rename_image, blank=True)
    adresse = models.CharField(max_length=20, null=True)
    membre = models.BooleanField(default=False)
    budget = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Membres(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Membre"
        verbose_name_plural = "Membres"

    def __str__(self):
        return str(self.user)

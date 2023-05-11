from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from membres.models import Membres

User = get_user_model()


@receiver(pre_save, sender=User)
def change_membre(sender, instance, **kwargs):

    if instance.budget == None:
        pass
    elif instance.budget >= 10000:
        instance.membre = True
        if not Membres.objects.filter(user=instance).exists():
            obj = Membres.objects.create(user=instance, price=instance.budget)
            obj.save()
        else:
            pass

# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from .models import Membres
# from django.contrib.auth import get_user_model

# User = get_user_model


# @receiver(pre_save, sender=User)
# def change_member(sender, instance, **kwargs):
#     if instance.budget >= 10000:
#         obj = Membres.objects.create(user=instance, price=instance.budget)
#         obj.save()
#     else:
#         pass

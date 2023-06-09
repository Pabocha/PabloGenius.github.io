# Generated by Django 4.2.1 on 2023-05-05 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utilisateurs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_de_profile', models.ImageField(blank=True, null=True, upload_to=utilisateurs.models.rename_image)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

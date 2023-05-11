from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages

# Create your views here.


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        obj = Contacts.objects.create(
            name=name, email=email, subject=subject, message=message)
        obj.save()
        messages.success(
            request, 'votre message à été reçu vous aurez une réponse dans maximum 24h par email soyer connecter')
        return redirect('contact')

    return render(request, 'base/contact.html')

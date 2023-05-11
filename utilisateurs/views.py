from django.shortcuts import render, HttpResponse, redirect
from .models import Utilisateur
from .forms import UserCreationForms
from django.contrib import messages

# Create your views here.


def register(request):
    form = UserCreationForms
    if request.method == 'POST':
        form = UserCreationForms(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['first_name']
            messages.success(
                request, f'votre comtpe à été créer avec success {user}')
            return redirect('home')

    context = {'form': form}

    return render(request, 'user_auth/register.html', context)

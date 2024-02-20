from django.shortcuts import render, redirect
from .models import *

from .forms import *

# Create your views here.

def user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = UsuarioForm()
    return render(request, 'account/registro.html', {'form': form})



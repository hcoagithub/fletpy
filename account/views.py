from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import authenticate, login

from .forms import *

# Create your views here.

def user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al usuario a la página deseada después del inicio de sesión exitoso
            return redirect('account:registro')  # Ajusta 'dashboard' según tus necesidades
        else:
            # Si la autenticación falla, puedes manejarlo de alguna manera, por ejemplo, mostrar un mensaje de error
            return render(request, 'login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos'})
    else:
        # Si la solicitud no es de tipo POST, simplemente renderiza el formulario de inicio de sesión
        return render(request, 'login.html')



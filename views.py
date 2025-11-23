from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Sala
from .forms import SalaForm

# ------------ HOME ----------------
def home(request):
    return render(request, 'home.html')

# ------------ LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "auth/login.html")

# ------------ LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')

# ------------ REGISTRO ----------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        from .models import Usuario
        user = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Registrado correctamente. Inicia sesión.")
        return redirect('login')

    return render(request, "auth/register.html")

# ------------ DASHBOARD ----------------
def dashboard(request):
    return render(request, "dashboard.html")

# ------------ CRUD SALAS ----------------
def salas_list(request):
    salas = Sala.objects.all()
    return render(request, 'salas/lista.html', {'salas': salas})

def salas_crear(request):
    form = SalaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('salas_list')
    return render(request, 'salas/crear.html', {'form': form})

def salas_editar(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    form = SalaForm(request.POST or None, instance=sala)
    if form.is_valid():
        form.save()
        return redirect('salas_list')
    return render(request, 'salas/editar.html', {'form': form})

def salas_eliminar(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    sala.delete()
    return redirect('salas_list')

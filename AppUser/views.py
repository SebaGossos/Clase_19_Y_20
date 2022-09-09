from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from AppUser.forms import UserRegisterForm


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data # me limpia la data que no necesito y me crea un diccionario

            usuario = data.get('username') # otra forma de acceder a la value de una key es usuario = data ['username']
            contrasenia = data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info (request, 'Inicio de sesion satifactorio')
                
            else:
                messages.info(request,'Por favor corroborar su usuario o contraseña!')
                
        else:
            messages.info(request,'Inicio de sesion fallido!')
                
        return redirect('AppsInicio')

    context = {
        'form': AuthenticationForm(),
        'name_submit': 'Login'
        
    }
    return render(request, 'AppUser/login.html', context)

def register(request):
    if request.method == 'POST':
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.info (request, 'Tu usuario fue registrado satisfactoriamente')
            
        else:
            
            messages.info(request, 'Tu usuario no pudo ser registrado')
        
        return redirect('AppsInicio')

    context = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'name_submit':'Registrarse'
    }
    
    return render(request, 'AppUser/login.html', context)
    
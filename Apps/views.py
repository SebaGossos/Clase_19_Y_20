from django.shortcuts import render, redirect
from Apps.models import Curso, Entregable
from Apps.forms import CursoFormulario, BusquedaCamadaFormulario
import datetime

def busqueda_camada_post(request):
    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    context = {
        'cursos': cursos
    }
    return render(request, 'TempApps/curso_filtrado.html', context)

def busqueda_camada(request):

    context = {
        'form': BusquedaCamadaFormulario(),
    }

    return render(request, 'TempApps/busqueda_camada.html', context)


def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso1.save()

            return redirect('AppsFormularioCurso')

    cursos = Curso.objects.all()
    context = {
        'form': CursoFormulario(),
        'cursos': cursos
    }

    return render(request, 'TempApps/cursoFormulario.html', context)


def inicio(request):
    contexto = {
        'valor1': 'este es un valor'
    }
    return render(request, 'index.html', contexto)

def curso(request):
    curso1 = Curso(nombre='Python', camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1,
    }
    return render(request, 'TempApps/curso.html', contexto)
def entregable(request):
    year = 2000
    month = 10
    day = 21

    entregable1 = Entregable(
        nombre='Luis',
        FechaDeEntrega=datetime.date(year=year, month=month, day=day),
        Entregado=True
    )
    entregable1.save()
    contexto ={
        'entregable': entregable1
    }
    return render(request,'TempApps/entregable.html', contexto)


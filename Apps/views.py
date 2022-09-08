from django.shortcuts import render, redirect
from Apps.models import Curso, Entregable
from Apps.forms import CursoFormulario, BusquedaCamadaFormulario
import datetime
from django.contrib import messages
import django
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class CursoList(ListView):
    model = Curso
    template_name = 'TempApps/curso.html'

# class CursoDetalle(DetailView):
#     model: Curso
#     template_name: 


def editar_curso(request, camada):
    curso_editar = Curso.objects.get(camada=camada) # aca abri mi base de datos

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            curso_editar.nombre = data.get('nombre') # Aca le digo a mi base de datos que me edite mi nombre
            curso_editar.camada = data.get('camada')
            try:

                curso_editar.save()

            except django.db.utils.IntegrityError:

                messages.error(request, 'La modificación fallo por que la camada esta repetida')



            return redirect('AppsFormularioCurso')

    context = {
        'form': CursoFormulario(
            initial = {
                'nombre': curso_editar.nombre,
                'camada': curso_editar.camada,
            }
        )
    }
    return render(request, 'TempApps/cursoFormulario.html', context)


def eliminar_curso (request, camada):
    curso_eliminar = Curso.objects.get(camada=camada)
    curso_eliminar.delete()
    
    messages.info(request, f'El curso: {curso_eliminar} fue eliminado')

    return redirect('AppsCurso')

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

    
    context = {
        'form': CursoFormulario(),
    }

    return render(request, 'TempApps/cursoFormulario.html', context)


def inicio(request):
    contexto = {
        'valor1': 'este es un valor'
    }
    return render(request, 'index.html', contexto)

# def curso(request):
#     lens = len(Curso.objects.all())
#     # cursos = Curso.objects.all()[lens-1:lens] # Es para que me traiga en ultimo curso guardado de mi bd
#     cursos = Curso.objects.all()
#     context = {
#        'cursos': cursos
#     }
#     return render(request, 'TempApps/curso.html', context)

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


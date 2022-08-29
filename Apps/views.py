from django.shortcuts import render
from Apps.models import Curso, Entregable
from datetime import datetime

def curso(request):
    curso1 = Curso(nombre='Python', camada=31095)
    #curso1.save()
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
        entregado=True
    )
    #entregable1.save()
    contexto ={
        'entregable': entregable1
    }
    return render(request,'TempApps/entregable.html', contexto)
from django.urls import path
from Apps.views import curso, entregable, inicio

urlpatterns = [
    path('Curso/', curso, name='AppsCurso'),
    path('Entregable/',entregable, name='AppsEntregable'),
    path('', inicio)
]
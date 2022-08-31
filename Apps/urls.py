from django.urls import path
from Apps.views import curso, entregable, inicio, cursoFormulario, busqueda_camada, busqueda_camada_post

urlpatterns = [
    path('Curso/', curso, name='AppsCurso'),
    path('cursoFormulario/',cursoFormulario, name='AppsFormularioCurso'),
    path('Entregable/',entregable, name='AppsEntregable'),
    path('', inicio, name='AppsInicio'),
    path('busquedaCamada/',busqueda_camada, name='AppsBusquedaCamada'),
    path('busquedaCamadaPost/',busqueda_camada_post, name='AppsBusquedaCamadaPost'),
]
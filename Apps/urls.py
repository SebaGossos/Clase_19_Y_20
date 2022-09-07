from django.urls import path
from Apps.views import *

urlpatterns = [
    path('Curso/', curso, name='AppsCurso'),
    path('cursoFormulario/',cursoFormulario, name='AppsFormularioCurso'),
    path('Entregable/',entregable, name='AppsEntregable'),
    path('', inicio, name='AppsInicio'),
    path('busquedaCamada/',busqueda_camada, name='AppsBusquedaCamada'),
    path('busquedaCamadaPost/',busqueda_camada_post, name='AppsBusquedaCamadaPost'),
    path('eliminar_curso/<int:camada>', eliminar_curso, name='AppsEliminarCurso'),
    path('editar_curso/<int:camada>', editar_curso, name='AppsEditarCurso'),
]
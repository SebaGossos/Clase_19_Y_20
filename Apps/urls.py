from django.urls import path
from Apps.views import curso, entregable

urlpatterns = [
    path('Curso/', curso),
    path('Entregable/',entregable)
]
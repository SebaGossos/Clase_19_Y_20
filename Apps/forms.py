from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=33)
    camada = forms.IntegerField()


class BusquedaCamadaFormulario(forms.Form):
    camada = forms.IntegerField()

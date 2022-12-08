from django import forms


class Proyectoform(forms.Form):

    Foto=forms.URLField()
    Titulo_del_proyecto=forms.CharField(max_length=30)
    Descripcion=forms.CharField(max_length=50)
    Tags=forms.CharField(max_length=30)
    url=forms.URLField()

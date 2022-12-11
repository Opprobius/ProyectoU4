from django import forms



class ProyectoForm(forms.Form):

    foto=forms.URLField()
    titulo_del_proyecto=forms.CharField(max_length=30)
    descripcion=forms.CharField(max_length=50)
    tags=forms.CharField(max_length=30)
    url=forms.URLField()


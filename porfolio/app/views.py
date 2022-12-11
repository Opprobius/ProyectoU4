from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import  CreateView
from .forms import ProyectoForm
from .models import Proyecto
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(View):
    def get(self, request):
        form=ProyectoForm()
        mostrar=Proyecto.objects.all()

        return render(request, "index.html", context={"formulario": form, "mostrar":mostrar})
    def post(self,request):
        form = ProyectoForm(request.POST)
        mostrar = Proyecto.objects.all()
        if form.is_valid():
            Proyecto.objects.create(
            foto=form.cleaned_data['foto'],
            titulo = form.cleaned_data['titulo_del_proyecto'],
            descripcion = form.cleaned_data['descripcion'],
            tags = form.cleaned_data['tags'],
            urls= form.cleaned_data['url']
            )
            return render(request, "index.html", context={"formulario": form, "mostrar":mostrar})
        else:
            return redirect('crear_item')




from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import Template, Context
from django.template import loader
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

def home(request):
    return render(request, "aplicacion/home.html")

def cursos(request):
    return render(request, "aplicacion/cursos.html")

def profesores(request):
    contexto = {'profesores': Profesor.objects.all()}
    return render(request, "aplicacion/profesores.html", contexto)

def estudiantes(request):
    return render(request, 'aplicacion/estudiantes.html')

def entregables(request):
    return render(request, 'aplicacion/entregables.html')

def crear_profesor(request):    
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_apellido = miForm.cleaned_data.get('apellido')
            p_email = miForm.cleaned_data.get('email')
            p_profesion = miForm.cleaned_data.get('profesion')
            profesor = Profesor(nombre=p_nombre, 
                             apellido=p_apellido,
                             email=p_email,
                             profesion=p_profesion,
                             )
            profesor.save()
            return redirect(reverse_lazy('profesores'))
    else:
        miForm = ProfesorForm()
    
    return render(request, "aplicacion/profesorForm.html", {"form":miForm})
    
def eliminar_profesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    return redirect(reverse_lazy('profesores'))

def modificar_profesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get('nombre')
            profesor.apellido = miForm.cleaned_data.get('apellido')
            profesor.email = miForm.cleaned_data.get('email')
            profesor.profesion = miForm.cleaned_data.get('profesion') 
            profesor.save()
            return redirect(reverse_lazy('profesores'))   
    else:
        miForm = ProfesorForm(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
        })
    return render(request, "aplicacion/profesorForm.html", {'form': miForm})

class CursoList(ListView):
    model = Curso

class CursoCreate(CreateView):
    model = Curso
    fields = ['nombre', 'comision']
    success_url = reverse_lazy('cursos')

class CursoUpdate(UpdateView):
    model = Curso
    fields = ['nombre', 'comision']
    success_url = reverse_lazy('cursos')

class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')
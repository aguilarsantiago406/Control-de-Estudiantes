from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Estudiante
from .forms import EstudianteForm


def lista(request):
    estudiantes = Estudiante.objects.all().order_by('id')
    return render(request, 'estudiantes/lista.html', {"estudiantes": estudiantes})


def detalle(request, pk):
    est = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiantes/detalle.html', {"est": est})


def crear(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()    
            messages.success(request, 'Estudiante creado correctamente')
            return redirect('estudiantes:lista')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/form.html', {"form": form, "titulo": "Nuevo Estudiante"})


def editar(request, pk):
    est = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=est)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante actualizado')
            return redirect('estudiantes:lista')
    else:
        form = EstudianteForm(instance=est)
    return render(request, 'estudiantes/form.html', {"form": form, "titulo": "Editar Estudiante"})


def eliminar(request, pk):
    est = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        est.delete()
        messages.success(request, 'Estudiante eliminado')
        return redirect('estudiantes:lista')
    return render(request, 'estudiantes/confirmar_eliminar.html', {"est": est})
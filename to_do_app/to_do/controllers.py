from django.shortcuts import render, get_object_or_404, redirect
from .models import LaClaseEsaDelModelo
from .views import LaClaseEsaDeLaVista

def show(request):
    cosas = LaClaseEsaDelModelo.objects.all()
    return render(request, 'show.html', {'cosas': cosas})

def add(request):
    if request.method == 'POST':
        form = LaClaseEsaDeLaVista(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = LaClaseEsaDeLaVista()
    return render(request, 'add.html', {'form': form})

def edit(request, producto_id):
    cosas = get_object_or_404(LaClaseEsaDelModelo, id=producto_id)
    if request.method == 'POST':
        form = LaClaseEsaDeLaVista(request.POST, instance=cosas)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = LaClaseEsaDeLaVista(instance=cosas)
    return render(request, 'editar_producto.html', {'form': form})

def delete(request, producto_id):
    cosas = get_object_or_404(LaClaseEsaDelModelo, id=producto_id)
    if request.method == 'POST':
        cosas.delete()
        return redirect('show')
    return render(request, 'delete.html', {'cosas': cosas})
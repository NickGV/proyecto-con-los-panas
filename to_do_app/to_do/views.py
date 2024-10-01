from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import tasks

class TaskListView(ListView):
    model = tasks
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = tasks
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = tasks
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = tasks
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

def task_complete(request, pk):
    task = get_object_or_404(tasks, pk=pk)
    task.status = 'Completed'
    task.save()
    return redirect('task_list')

# Create your views here.

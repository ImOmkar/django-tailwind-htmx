from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, TaskUpdateForm
from django.http import HttpResponseRedirect
from core.models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
        'title': "TO-DO - Home"
    }
    return render(request, "home.html", context)


def task_list(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
        'title': "Home"
    }
    return render(request, "tasks_list.html", context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks_create.html', {'form': form})
 

def update_task(request, id):
    obj = get_object_or_404(Task, id=id)
    edit_form = TaskUpdateForm(request.POST or None, instance=obj)

    if edit_form.is_valid():
        edit_form.save()
        return redirect('home')
    
    context = {
        'obj': obj,
        'edit_form': edit_form
    }

    return render(request, "tasks_update.html", context)


def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks_list.html', {'tasks': tasks})
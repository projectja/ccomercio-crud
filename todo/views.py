from django.shortcuts import render, redirect
from .models import Tarea, Projects
from .forms import TareaForm, ProjectsForm
from openpyxl import LXML, load_workbook


# Create your views here.

def home(request):
    form = ProjectsForm
    projects = Projects.objects.all()
    context = {'form': form, 'projects': projects}
    return render(request, 'todo/home.html', context)

# CRUD - ADD
def agregar(request):
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectsForm()

    context = {'form': form}
    return render(request, 'todo/agregar.html', context)

# CRUD - DELETE
def eliminar(request, tarea_id):
    project = Projects.objects.get(id=tarea_id)
    project.delete()
    return redirect("home")

# CRUD - EDIT
def editar(request, tarea_id):
    project = Projects.objects.get(id=tarea_id)
    if request.method == "POST":
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectsForm(instance=project)

    context = {'form': form}
    return render(request, "todo/editar.html", context)

# ON-DEMAND ACTION OVER SELECTED DOCUMENTS
def generar_doc2(request, tarea_id):
    form = ProjectsForm(request.POST, instance=project)
    context = {'form': form}
    return render(request, "todo/generar_doc.html", context)

def generardoc(request):
    project = Projects.objects.get(id=3)
    print("holaaaa")
    if request.method == "POST":
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            print("dentro del form")
            form.save()
            return redirect('home')
    else:
        form = ProjectsForm(instance=project)

    context = {'form': form}
    return render(request, "todo/generardoc.html", context)


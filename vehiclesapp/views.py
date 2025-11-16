from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import VehicleForm
from .models import vehiculo

# CREATE
def create_view(request):
    context = {}
    form = VehicleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "create_view.html", context)


# READ (LISTAR)
def list_view(request):
    context = {}
    context["dataset"] = vehiculo.objects.all()
    return render(request, "list_view.html", context)


# UPDATE
def update_view(request, id):
    context = {}
    obj = get_object_or_404(vehiculo, id=id)
    form = VehicleForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "update_view.html", context)


# DELETE
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(vehiculo, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

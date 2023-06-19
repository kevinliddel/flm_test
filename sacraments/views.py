from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import (
    SacramentsForm
)
from .models import Sacraments


# ########################################################
# sacrament views
# ########################################################

def sacrament_view(request):
    sacraments = Sacraments.objects.all()
    paginator = Paginator(sacraments, 10)
    page_number = request.GET.get('page')
    sacraments = paginator.get_page(page_number)

    sacrament_filter = request.GET.get('sacrament_filter')
    if sacrament_filter:
        sacraments = Sacraments.objects.filter(name__icontains=sacrament_filter)

    return render(request, 'sacraments/sacrament_list.html', {
        'title': "Liste des chrétiens ayant fait leur confirmation",
        'sacraments': sacraments,
    })
    

def sacrament_add(request):
    if request.method == 'POST':
        form = SacramentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, request.POST.get('name') + ' a été ajouté à la liste des chrétiens ayant fait leur confirmation.')
            return redirect('sacraments')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = SacramentsForm()

    return render(request, 'sacraments/sacrament_add.html', {
        'title': "Ajouter un membre ayant fait sa confirmation",
        'form': form,
    })
    

def sacrament_edit(request, pk):
    sacrament = Sacraments.objects.get(pk=pk)

    if request.method == 'POST':
        form = SacramentsForm(request.POST, instance=sacrament)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations à propos de cette confirmation ont bien été mise à jour')
            return redirect('sacraments')
    else:
        form = SacramentsForm(instance=sacrament)

    return render(request, 'sacraments/sacrament_edit.html', {
        'title': "Modifier les informations à propos de cette confirmation",
        'form': form
    })



def sacrament_delete(request, pk):
    sacrament = Sacraments.objects.get(pk=pk)
    name = sacrament.name
    sacrament.delete()
    messages.success(request, 'Les informations à propos de la confirmation de ' + name + ' ont été supprimé avec succès.')

    return redirect('sacraments')
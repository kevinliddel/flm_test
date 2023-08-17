from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import (
    SacramentsForm
)
from .models import Sacraments


# ########################################################
# sacrament views
# ########################################################
@login_required
@never_cache
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
    
@login_required
@never_cache
def sacrament_add(request):
    if request.method == 'POST':
        form = SacramentsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
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
    
@login_required
@never_cache
def sacrament_edit(request, pk):
    sacrament = Sacraments.objects.get(pk=pk)

    if request.method == 'POST':
        form = SacramentsForm(request.POST, instance=sacrament)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Les informations à propos de cette confirmation ont bien été mise à jour')
            return redirect('sacraments')
    else:
        form = SacramentsForm(instance=sacrament)

    return render(request, 'sacraments/sacrament_edit.html', {
        'title': "Modifier les informations à propos de cette confirmation",
        'form': form
    })


@login_required
@never_cache
def sacrament_delete(request, pk):
    sacrament = Sacraments.objects.get(pk=pk)
    name = sacrament.name
    sacrament.delete()
    messages.success(request, 'Les informations à propos de la confirmation de ' + name + ' ont été supprimé avec succès.')

    return redirect('sacraments')

@login_required
@never_cache
def delete_sacrament(request, pk):
    if request.method == 'POST':
        sacrament = get_object_or_404(Sacraments, pk=pk)
        sacrament.delete()
    return redirect('sacraments')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import (
    BaptismsForm
)
from .models import Baptisms
from members.models import Members


# ########################################################
# baptism views
# ########################################################
@login_required
@never_cache
def baptism_view(request):
    baptisms = Baptisms.objects.all()
    paginator = Paginator(baptisms, 10)
    page_number = request.GET.get('page')
    baptisms = paginator.get_page(page_number)

    baptism_filter = request.GET.get('baptism_filter')
    if baptism_filter:
        baptisms = Baptisms.objects.filter(name__icontains=baptism_filter)

    return render(request, 'baptisms/baptism_list.html', {
        'title': "Liste des chrétiens ayant été baptisés",
        'baptisms': baptisms,
    })
    
@login_required
@never_cache
def baptism_add(request):
    if request.method == 'POST':
        form = BaptismsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, request.POST.get('name') + ' a été ajouté à la liste des chrétiens ayant été baptisés.')
            return redirect('baptisms')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = BaptismsForm()

    return render(request, 'baptisms/baptism_add.html', {
        'title': "Ajouter un membre baptisé",
        'form': form,
    })
    
@login_required
@never_cache
def baptism_edit(request, pk):
    baptism = Baptisms.objects.get(pk=pk)

    if request.method == 'POST':
        form = BaptismsForm(request.POST, instance=baptism)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Les informations à propos de ce baptême ont bien été mise à jour')
            return redirect('baptisms')
    else:
        form = BaptismsForm(instance=baptism)

    return render(request, 'baptisms/baptism_edit.html', {
        'title': "Modifier les informations à propos du baptême",
        'form': form
    })


@login_required
@never_cache
def baptism_delete(request, pk):
    baptism = Baptisms.objects.get(pk=pk)
    name = baptism.name
    baptism.delete()
    messages.success(request, 'Les informations à propos du baptême de ' + name + ' ont été supprimé avec succès.')

    return redirect('baptisms')

@login_required
@never_cache
def delete_baptism(request, pk):
    if request.method == 'POST':
        baptism = get_object_or_404(Baptisms, pk=pk)
        baptism.delete()
    return redirect('baptisms')
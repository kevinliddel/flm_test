from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import (
    MinistriesForm
)
from .models import Ministries


# ########################################################
# ministry views
# ########################################################

def ministry_view(request):
    ministries = Ministries.objects.all()
    paginator = Paginator(ministries, 10)
    page_number = request.GET.get('page')
    ministries = paginator.get_page(page_number)

    ministry_filter = request.GET.get('ministry_filter')
    if ministry_filter:
        ministries = Ministries.objects.filter(name__icontains=ministry_filter)

    return render(request, 'ministries/ministry_list.html', {
        'title': "Liste des personnes servant à l'église",
        'ministries': ministries,
    })
    
@login_required
@never_cache
def ministry_add(request):
    if request.method == 'POST':
        form = MinistriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, request.POST.get('name') + ' a été ajouté à la liste des personnes servant à l\'église.')
            return redirect('ministries')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = MinistriesForm()

    return render(request, 'ministries/ministry_add.html', {
        'title': "Ajouter un nouveau employé",
        'form': form,
    })
    
@login_required
@never_cache
def ministry_edit(request, pk):
    ministry = Ministries.objects.get(pk=pk)

    if request.method == 'POST':
        form = MinistriesForm(request.POST, instance=ministry)
        if form.is_valid():
            form.save()
            messages.success(request, str(request.POST.get('name')) + ' a bien été modifié.')
            return redirect('ministries')
    else:
        form = MinistriesForm(instance=ministry)

    return render(request, 'ministries/ministry_edit.html', {
        'title': "Modifier l'employé",
        'form': form
    })


@login_required
@never_cache
def ministry_delete(request, pk):
    ministry = Ministries.objects.get(pk=pk)
    name = ministry.name
    ministry.delete()
    messages.success(request, 'L\'employé du nom de ' + name + ' a été supprimé avec succès.')

    return redirect('ministries')

@login_required
@never_cache
def delete_ministry(request, pk):
    if request.method == 'POST':
        ministry = get_object_or_404(Ministries, pk=pk)
        ministry.delete()
    return redirect('ministries')
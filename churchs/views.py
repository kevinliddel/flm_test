from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import (
    ChurchsForm
)
from .models import Churchs


# ########################################################
# church views
# ########################################################

def church_view(request):
    churchs = Churchs.objects.all()
    paginator = Paginator(churchs, 10)
    page_number = request.GET.get('page')
    churchs = paginator.get_page(page_number)

    church_filter = request.GET.get('church_filter')
    if church_filter:
        churchs = Churchs.objects.filter(church_name__icontains=church_filter)

    return render(request, 'churchs/church_list.html', {
        'title': "Liste des églises",
        'churchs': churchs,
    })
    

def church_add(request):
    if request.method == 'POST':
        form = ChurchsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, request.POST.get('church_name') + ' a été ajouté à la liste des églises.')
            return redirect('churchs')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = ChurchsForm()

    return render(request, 'churchs/church_add.html', {
        'title': "Ajouter une nouvelle église",
        'form': form,
    })
    

def church_edit(request, pk):
    church = Churchs.objects.get(pk=pk)

    if request.method == 'POST':
        form = ChurchsForm(request.POST, instance=church)
        if form.is_valid():
            form.save()
            messages.success(request, str(request.POST.get('church_name')) + ' a bien été modifié.')
            return redirect('churchs')
    else:
        form = ChurchsForm(instance=church)

    return render(request, 'churchs/church_edit.html', {
        'title': "Modifier l'église",
        'form': form
    })



def church_delete(request, pk):
    church = Churchs.objects.get(pk=pk)
    church_name = church.church_name
    church.delete()
    messages.success(request, 'L\'église ' + church_name + ' a été supprimé avec succès.')

    return redirect('churchs')
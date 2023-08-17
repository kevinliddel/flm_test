from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import (
    ChurchsForm
)
from .models import Churchs

from django.http import JsonResponse

from places.models import Places


# ########################################################
# church views
# ########################################################
@login_required
@never_cache
def church_view(request):
    churchs = Churchs.objects.all()
    countries = Places.objects.values_list('country', flat=True).distinct()
    paginator = Paginator(churchs, 10)
    page_number = request.GET.get('page')
    churchs = paginator.get_page(page_number)

    church_filter = request.GET.get('church_filter')
    if church_filter:
        churchs = Churchs.objects.filter(church_name__icontains=church_filter)

    return render(request, 'churchs/church_list.html', {
        'title': "Liste des établissements de l'église",
        'churchs': churchs,
        'countries': countries,
    }) 

@login_required
@never_cache
def church_add(request):
    if request.method == 'POST':
        form = ChurchsForm(request.POST)
        if form.is_valid():
            church = form.save(commit=False)

            # Save the Churchs object without the dependent fields
            church.save()

            # Get the selected values from the dependent fields
            country_name = request.POST.get('country')
            district_name = request.POST.get('district')
            neighborhood_name = request.POST.get('neighborhood')
            street_name = request.POST.get('street')

            # Update the Churchs object with the selected values from the dependent fields
            church.country = country_name
            church.district = district_name
            church.neighborhood = neighborhood_name
            church.street = street_name

            # Save the Churchs object again with the dependent fields
            church.save()

            messages.success(request, church.church_name + ' a été ajouté à la liste des églises.')
            return redirect('churchs')
        else:
            print("Form errors:", form.errors)
    else:
        form = ChurchsForm()

    return render(request, 'churchs/church_add.html', {
        'title': "Ajouter un nouvel établissement",
        'form': form,
    })
       
@login_required
@never_cache
def church_edit(request, pk):
    church = Churchs.objects.get(pk=pk)

    if request.method == 'POST':
        form = ChurchsForm(request.POST, instance=church)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, str(request.POST.get('church_name')) + ' a bien été modifié.')
            return redirect('churchs')
    else:
        form = ChurchsForm(instance=church)

    return render(request, 'churchs/church_edit.html', {
        'title': "Modifier cet établissement",
        'form': form
    })


@login_required
@never_cache
def church_delete(request, pk):
    church = Churchs.objects.get(pk=pk)
    church_name = church.church_name
    church.delete()
    messages.success(request, 'L\'église ' + church_name + ' a été supprimé avec succès.')

    return redirect('churchs')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import (
    MembersForm
)
from .models import Members


# ########################################################
# member views
# ########################################################

def member_view(request):
    members = Members.objects.all()
    paginator = Paginator(members, 10)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)

    member_filter = request.GET.get('member_filter')
    if member_filter:
        members = Members.objects.filter(name__icontains=member_filter)

    return render(request, 'members/member_list.html', {
        'title': "Liste des membres de l'église",
        'members': members,
    })
    

def member_add(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, request.POST.get('name') + ' a été ajouté à la liste des membres de l\'église.')
            return redirect('members')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = MembersForm()

    return render(request, 'members/member_add.html', {
        'title': "Ajouter un nouveau membre",
        'form': form,
    })
    

def member_edit(request, pk):
    member = Members.objects.get(pk=pk)

    if request.method == 'POST':
        form = MembersForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, str(request.POST.get('name')) + ' a bien été modifié.')
            return redirect('members')
    else:
        form = MembersForm(instance=member)

    return render(request, 'members/member_edit.html', {
        'title': "Modifier du membre",
        'form': form
    })



def member_delete(request, pk):
    member = Members.objects.get(pk=pk)
    name = member.name
    member.delete()
    messages.success(request, 'Le membre du nom de ' + name + ' a été supprimé avec succès.')

    return redirect('members')
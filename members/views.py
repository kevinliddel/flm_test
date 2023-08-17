from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import (
    MembersForm
)
from .models import Members

# from dal import autocomplete

# ########################################################
# member views
# ########################################################
@login_required
@never_cache
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

@login_required
@never_cache
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
    
@login_required
@never_cache
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


@login_required
@never_cache
def member_delete(request, pk):
    member = Members.objects.get(pk=pk)
    name = member.name
    member.delete()
    messages.success(request, 'Le membre du nom de ' + name + ' a été supprimé avec succès.')

    return redirect('members')

#class MemberAutocomplete(autocomplete.Select2QuerySetView):
#    def get_queyset(self):
#        qs = Members.objects.all()
#        
#        if self.q:
#            qs = qs.filter(name__istartswith=self.q)
#            
#        return qs

@login_required
@never_cache
def delete_member(request, pk):
    if request.method == 'POST':
        member = get_object_or_404(Members, pk=pk)
        member.delete()
    return redirect('members')
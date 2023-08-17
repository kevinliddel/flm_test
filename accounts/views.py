from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView, ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .decorators import admin_required
from .forms import CustomForm, ProfileUpdateForm
from .models import User, Custom


def validate_username(request):
    username = request.GET.get("username", None)
    data = {
        "is_taken": User.objects.filter(username__iexact = username).exists()
    }
    return JsonResponse (data)
# ########################################################


# ########################################################
# Setting views
# ########################################################
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a bien été modifié avec succès.')
            return redirect('home')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivants.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'setting/profile_info_change.html', {
        'title': 'Paramètre',
        'form': form,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été modifié avec succès!')
            return redirect('home')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivants. ')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'setting/password_change.html', {
        'title': 'Changer le mot de passe',
        'form': form,
    })

# ########################################################
# Custom views
# ########################################################
@login_required
@admin_required
def add(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            form.save()
            messages.success(request, 'Le compte pour l\'utilisateur ' + first_name + ' ' + last_name + ' a été créé')
            return redirect('list')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = CustomForm()

    return render(request, 'accounts/add.html', {
        'title': "Ajouter un utilisateur",
        'form': form
    })


@login_required
@admin_required
def edit(request, pk):
    # instance = User.objects.get(pk=pk)
    instance = get_object_or_404(User, is_customuser=True, pk=pk)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=instance)
        full_name = instance.get_full_name
        if form.is_valid():
            form.save()

            messages.success(request, ('L\'utilisateur ' + full_name + ' a bien été modifié.'))
            return redirect('list')
        else:
            messages.error(request, 'Veuillez corriger les erreurs suivantes.')
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(request, 'accounts/edit.html', {
        'title': 'Modifier l\'utilisateur',
        'form': form,
    })


@method_decorator([login_required], name='dispatch')
class CustomUserList(ListView):
    template_name = "accounts/list.html"
    paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        queryset = Custom.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Liste des utilisateurs"
        return context

@login_required
@admin_required
def delete(request, pk):
    custom = get_object_or_404(Custom, pk=pk)
    custom.delete()
    messages.success(request, 'L\'utilisateur a été supprimé avec succès.')
    return redirect('list')

@login_required
def delete_custom(request, pk):
    if request.method == 'POST':
        custom = get_object_or_404(Custom, pk=pk)
        custom.delete()
    return redirect('customs')
# ########################################################

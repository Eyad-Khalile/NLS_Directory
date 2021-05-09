import urllib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import CountryForm
from .models import Countries
from django.utils.timezone import datetime
from django.contrib.auth.decorators import login_required


# COUNTRIES LIST
@login_required(login_url='user_login')
def countries_list(request):
    countries = Countries.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'map_app/countries/list.html', context)


# CREATE COUNTRY
@login_required(login_url='user_login')
def countries_add(request):
    if request.method == 'POST':
        form = CountryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'the country has been added successfuly :) ')
            return redirect('countries_add')
    else:
        form = CountryForm()
    context = {
        'form': form,
    }
    return render(request, 'map_app/countries/add.html', context)


# DETAILS OF COUNTRY
@login_required(login_url='user_login')
def country_details(request, id):
    country = get_object_or_404(Countries, id=id)

    context = {
        'country': country,
    }
    return render(request, 'map_app/countries/details.html', context)

# UPDATE COUNTRY


@login_required(login_url='user_login')
def country_edit(request, id):
    country = get_object_or_404(Countries, id=id)
    if request.method == 'POST':
        form = CountryForm(request.POST or None, instance=country)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.updated_at = datetime.utcnow()
            inst.save()
            messages.success(
                request, 'the country has been updated successfuly :) ')
            return redirect('countries_list')
    else:
        form = CountryForm(instance=country)

    context = {
        'country': country,
        'form': form,
    }
    return render(request, 'map_app/countries/edit.html', context)


# DELETE COUNTRY
@login_required(login_url='user_login')
def country_delete(request, id):
    country = get_object_or_404(Countries, id=id)
    if request.method == 'POST':
        country.delete()

        messages.success(
            request, 'the country has been deleted in successfuly')
        return redirect('home')

    context = {
        'country': country,
    }
    return render(request, 'map_app/countries/delete.html', context)

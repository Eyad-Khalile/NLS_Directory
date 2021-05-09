import urllib
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import NewOrgForm, ContactForm, AcceptCookieForm
from .models import Countries, Orgs
from django.utils.timezone import datetime
from cart.forms import CartAddOrgForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import EmailMessage
from .resources import OrgsResource
from tablib import Dataset

# MAP
import folium

# SET COOKIE ACCEPTATION
def set_cookie(request):
    path = request.POST.get("current_path")
    response = redirect(path)
    response.set_cookie('accept_cookie', True, max_age=60 * 60 * 24 * 10)
    return response

# HOME-PAGE
def home(request):
    formCookie = AcceptCookieForm()
    accept_cookie = request.COOKIES.get('accept_cookie', False)
    orgs_list = Orgs.objects.all().order_by('order_by')
    countries = Countries.objects.all()

    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)

    context = {
        'orgs_list': orgs_list,
        'countries': countries,
        'cart_orgs': cart_orgs,
        'formCookie': formCookie,
        'accept_cookie': accept_cookie,

    }
    return render(request, 'map_app/home.html', context)


# THE WORLD MAP
def country_map(request, id):

    # GET CURRENT COUNTRY FROM DB
    country_clicked = get_object_or_404(Countries, pk=id)
    cuurent_country = [country_clicked.latitude, country_clicked.longitude]
    map_1 = folium.Map(location=cuurent_country,
                       zoom_start=4.5)

    orgs = Orgs.objects.all()
 
    for loc in orgs:
        if loc.full_address:
            org_address = loc.full_address
        else:
            org_address = loc.address
        btnDetails = f'<a href="/org_details/{loc.id}/" class="btn btn-info btn_details" target="_blank" style="width: 250px;"> Details </a>'
        folium.Marker(icon=folium.Icon(color='red'),
                      location=[loc.latitude, loc.longitude], tooltip=f"{loc.name}", popup=f'{loc.name}<hr />{org_address}<hr />{loc.primary_phone}<hr /> {btnDetails} ').add_to(map_1)

    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map_1)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map_1)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map_1)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(map_1)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(map_1)

    folium.LayerControl().add_to(map_1)
    map_1 = map_1._repr_html_()

    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)


    context = {
        'my_map': map_1,
        'cart_orgs': cart_orgs,
    }
    return render(request, 'map_app/country_map.html', context)


# CREATE ORG
@login_required(login_url='user_login')
def add_org(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = NewOrgForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'The Organisation has been added succesfuly')
                return redirect('add_org')
            else:
                messages.error(request, 'The form is not valide')
        else:
            form = NewOrgForm()
    else:
        messages.error(request, "You Don't have the permissions for this page")
        return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'map_app/org/add_org_form.html', context)


# DETAILS OF ORG
def org_details(request, id):
    org = get_object_or_404(Orgs, id=id)
    add_to_cart_form = CartAddOrgForm()

    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)

    context = {
        'org': org,
        'add_to_cart_form': add_to_cart_form,
        'cart_orgs': cart_orgs,
    }
    return render(request, 'map_app/org/org_details.html', context)


# UPDATE ORG
@login_required(login_url='user_login')
def org_update(request, id):
    org = get_object_or_404(Orgs, id=id)
    if request.user.is_authenticated and request.user.is_superuser: 
        if request.method == 'POST':
            form = NewOrgForm(request.POST or None, instance=org)
            if form.is_valid():
                inst = form.save(commit=False)
                inst.updated_at = datetime.utcnow()
                inst.save()

                messages.success(
                    request, 'The organisation has been updated succesfuly')
                return redirect(org)
            else:
                messages.error(request, 'The form is not valide')
        else:
            form = NewOrgForm(instance=org)
    else:
        messages.error(request, "You Don't have the permissions for this page")
        return redirect('home')

    context = {
        'org': org,
        'form': form,
    }
    return render(request, 'map_app/org/org_update.html', context)

# DELETE ORG
@login_required(login_url='user_login')
def org_delete(request, id):
    org = get_object_or_404(Orgs, id=id)
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            org.delete()
            messages.success(
                request, 'The orgnisation has been deleted succesfuly')
            return redirect('home')
    else:
        messages.error(request, "You Don't have the permissions for this page")
        return redirect('home')

    context = {
        'org': org,
    }
    return render(request, 'map_app/org/org_delete.html', context)


# FOOTER LIKES
def imprint(request):
    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)
    ctx = {
        'cart_orgs': cart_orgs,
    }
    return render(request, 'extra/imprint.html', ctx)


def data_policy(request):
    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)
    ctx = {
        'cart_orgs': cart_orgs,
    }
    return render(request, 'extra/data_policy.html', ctx)


def about(request):
    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)
    ctx = {
        'cart_orgs': cart_orgs,
    }
    return render(request, 'extra/about.html', ctx)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():

            contact_name = form.cleaned_data.get('contact_name')
            subject = form.cleaned_data.get('contact_subject')
            message = form.cleaned_data.get('contact_message')
            from_email = form.cleaned_data.get('contact_email')
            email = EmailMessage(
                subject, body=f'Name Of Sender : {contact_name} , The Message : {message}', to=['eyad.esgi@gmail.com'], reply_to=[from_email]
            )
            email.send()

            messages.success(
                request, f'Your Message has been sended Successful')

            return redirect('home')

    else:
        form = ContactForm()
        cart = Cart(request)
        my_cart_list = []
        for item in cart.cart:
            my_cart_list.append(item)
        cart_orgs = Orgs.objects.filter(pk__in=my_cart_list)
        
    ctx = {
        'form': form,
        'cart_orgs': cart_orgs,
    }
    return render(request, 'extra/contact.html', ctx)


# UPLOAD EXCEL FILES DATA
@login_required(login_url='user_login')
def simple_upload(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            orgs_resource = OrgsResource()
            dataset = Dataset()
            new_org = request.FILES['myfile']

            if not new_org.name.endswith('xlsx'):
                messages.error(request, 'Wrong Format')
                return render(request, 'extra/upload.html')
            else:
                imported_data = dataset.load(new_org.read(), format='xlsx')
                for data in imported_data:
                    value = Orgs(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                        data[9],
                        data[10],
                        data[11],
                        data[12],
                        data[13],
                        data[14],
                        data[15],
                        data[16],
                        data[17],
                        data[18],
                        data[19],
                        data[20],
                        data[21],
                        data[22],
                        data[23],
                        data[24],
                        data[25],
                        data[26],
                        data[27],
                        data[28],
                        data[29],
                        data[30],
                        data[31],
                        data[32],
                        data[33],
                        data[34],
                        data[35],
                        data[36],
                        data[37],
                        data[38],
                        data[39],
                        data[40],
                        data[41],
                        data[42],
                        data[43],
                        data[44],
                        data[45],
                        data[46],
                        data[47],
                        data[48],
                    )
                    value.save()
                    messages.success(
                        request, 'The data has been saved in the database succesfully')
    else:
        messages.error(request, "You Don't have the permissions for this page")
        return redirect('home')
    return render(request, 'extra/upload.html')


def error_404_view(request, exception):
    return render(request, 'errors/404.html')


def error_500_view(request, exception=None):
    return render(request, 'errors/500.html')

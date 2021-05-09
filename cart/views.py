from django.shortcuts import render, redirect, get_object_or_404
from map_app.models import *
from django.views.decorators.http import require_POST
from .forms import CartAddOrgForm, EmailForm
from .cart import Cart
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


@require_POST
def cart_add(request, org_id):
    cart = Cart(request)
    org = get_object_or_404(Orgs, id=org_id)

    form = CartAddOrgForm(request.POST)
    if form.is_valid():
        cart.add(org=org)
        messages.success(
            request, 'The Organisation has been added successfuly')
    return redirect('home')


def cart_remove(request, org_id):
    cart = Cart(request)
    org = get_object_or_404(Orgs, id=org_id)
    if request.method == 'POST':
        remove = request.POST.get("cart_remove_input")
        path = request.POST.get("current_path")
        if remove and path:
            cart.remove(org)
            messages.success(
                request, 'The Organasition has been deleted from the cart')
    # return redirect('cart:cart_detail')
    return redirect(path)


def cart_detail(request):
    cart = Cart(request)
    my_cart_list = []
    for item in cart.cart:
        my_cart_list.append(item)
    orgs = Orgs.objects.filter(pk__in=my_cart_list)

    if request.method == 'POST':
        form = EmailForm(request.POST or None)
        if form.is_valid():
            accept = form.cleaned_data.get('accept_policy')
            if accept == 'True':
                client_email = form.cleaned_data.get('email_to')
                current_site = get_current_site(request)
                subject = 'My results of searching'
                message = render_to_string('cart/results_email.html', {
                    'domain': current_site.domain,
                    'orgs': orgs,
                })
                to_email = form.cleaned_data.get('email_to')
                to_email = client_email
                email = EmailMessage(
                    subject, message, to=[to_email]
                )
                email.send()
                messages.success(
                    request, 'The email has been sent successfully')
            else:
                messages.error(
                    request, 'Please accept our data policy')
    else:
        form = EmailForm()

    return render(request, 'cart/detail.html', {'cart_orgs': orgs, 'form': form, })

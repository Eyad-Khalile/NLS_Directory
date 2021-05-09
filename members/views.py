from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import *
from .forms import *
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
import os
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.timezone import datetime
from django.db.models import Q
from django.utils.translation import gettext as _


def UserRegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            form = SignUpForm(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                subject = 'Activate Your Account.'
                message = render_to_string('registration/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    subject, message, to=[to_email]
                )
                email.send()
                username = form.cleaned_data.get('username')

                messages.success(
                    request, f'Your Account has been created Successful with username ( {username} ) !, Please confirm your email address to complete the registration ')

                return redirect('home')

        else:
            form = SignUpForm()

        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context)


# ACTIVATION ACCOUNT
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'register/active.html')


# SIGNE IN VIEW
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'The user is not active')
            else:
                messages.error(request, 'The user is not exist')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }

    return render(request, 'registration/login.html', context)



# EDIT USER PROFILE
@login_required(login_url='signe_in')
def UserEditView(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, instance=user)
        form_profile = ProfileUpdateForm(
            request.POST or None, request.FILES or None, instance=user.profile)
        if form.is_valid() and form_profile.is_valid():
            form.save()

            pic = form_profile.save(commit=False)
            pic.updated_at = datetime.utcnow()
            pic.save()

            messages.success(
                request, ('you have been updated your profile in successfuly'))

            return redirect('home')
    else:
        form = EditProfileForm(instance=user)
        form_profile = ProfileUpdateForm(instance=user.profile)

    context = {
        'form': form,
        'form_profile': form_profile,
    }
    return render(request, 'registration/edit_profile.html', context)


# CHANGE PASSWORD
# @login_required(login_url='signe_in')
class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


# CHANGE PASSWORD SUCCESS
# @login_required(login_url='signe_in')
def password_success(request):
    return render(request, 'registration/password-success.html')

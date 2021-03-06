from django.shortcuts import redirect

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

from django.views.decorators.http import require_http_methods

from rest_framework.authtoken.models import Token

import base64

from ...forms import SignInForm, SignUpForm, ProfileEditForm
from .views_handlers_functions import is_email_unique, send_verification_mail


@require_http_methods(["POST"])
def signin_handler(request):
    signin_form_data = SignInForm(request.POST)

    if signin_form_data.is_valid():
        email = signin_form_data.cleaned_data['email']
        password = signin_form_data.cleaned_data['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)

            return redirect('profile_page')
        else:

            request.session['errormessage_signin_data_wrong'] = True

            return redirect('index_page')


@require_http_methods(["POST"])
def signup_handler(request):
    signup_form_data = SignUpForm(request.POST)

    if signup_form_data.is_valid():
        email = signup_form_data.cleaned_data['email']
        password = signup_form_data.cleaned_data['password']

        if is_email_unique(request, email):
            return redirect('index_page')

        request.session["socialnetwork_verification"] = make_password(password)

        send_verification_mail(email, password)

        request.session['infomessage_emailsent'] = True
        return redirect('index_page')


def verify_user(request, email, password):
    decoded_password = base64.b64decode(password.encode('ascii')).decode('ascii')
    decoded_email = base64.b64decode(email.encode('ascii')).decode('ascii')

    if check_password(decoded_password, request.session.get('socialnetwork_verification')):
        user_model = get_user_model()

        user = user_model.objects.create_user(email=decoded_email, password=decoded_password)
        user.save()

        del request.session['socialnetwork_verification']

        request.session['infomessage_verified'] = True
        return redirect('index_page')
    else:
        request.session['errormessage_invalidverification'] = True
        return redirect('index_page')


@require_http_methods(["POST"])
def profile_edit_handler(request):
    profile_edit_form = ProfileEditForm(request.POST)

    if profile_edit_form.is_valid():
        first_name = profile_edit_form.cleaned_data['first_name']
        surname = profile_edit_form.cleaned_data['surname']

        current_user = request.user

        current_user.first_name = first_name
        current_user.surname = surname

        current_user.save()

        return redirect('profile_page')


def logout_handler(request):
    logout(request)

    return redirect('index_page')


def create_token(request):
    token = Token.objects.create(user=request.user)

    token.save()

    return redirect('api_page')


def delete_token(request):
    token = Token.objects.get(user=request.user)

    token.delete()

    return redirect('api_page')


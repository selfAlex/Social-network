from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.http import require_http_methods

from ..forms import SignInForm, SignUpForm


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
            sign_in_form = SignInForm()
            sign_up_form = SignUpForm()

            return render(request, 'app/index.html', {'signin_error_msg': True, 'sign_in_form': sign_in_form,
                                                      'sign_up_form': sign_up_form})


@require_http_methods(["POST"])
def signup_handler(request):
    signup_form_data = SignUpForm(request.POST)

    if signup_form_data.is_valid():
        email = signup_form_data.cleaned_data['email']
        password = signup_form_data.cleaned_data['password']

        user_model = get_user_model()

        user = user_model.objects.create_user(email=email, password=password)
        user.save()

        login(request, user)

        return render(request, 'app/profile.html', {'new_user_msg': True})


def logout_handler(request):
    logout(request)

    return redirect('index_page')

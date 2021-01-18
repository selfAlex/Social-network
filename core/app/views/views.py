from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import datetime


from ..forms import SignInForm, SignUpForm, ProfileEditForm


def index_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    else:
        sign_in_form = SignInForm()
        sign_up_form = SignUpForm()

    return render(request, 'app/index.html', {'sign_in_form': sign_in_form, 'sign_up_form': sign_up_form})


@login_required()
def profile_page(request):
    if request.user.date_joined is None:
        request.user.date_joined = datetime.now()
        request.user.password = None
        request.user.save()

    return render(request, 'app/profile.html')


def profile_edit_page(request):
    profile_edit_form = ProfileEditForm()
    return render(request, 'app/profile_edit.html', {'profile_edit_form': profile_edit_form})


def messenger_page(request):
    return render(request, 'app/messenger.html')


def api_page(request):
    return render(request, 'app/api.html')

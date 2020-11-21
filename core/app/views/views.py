from django.shortcuts import render, redirect
from ..forms import SignInForm, SignUpForm
from django.contrib.auth.decorators import login_required


def index_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    else:
        sign_in_form = SignInForm()
        sign_up_form = SignUpForm()

    return render(request, 'app/index.html', {'sign_in_form': sign_in_form, 'sign_up_form': sign_up_form})


@login_required()
def profile_page(request):
    return render(request, 'app/profile.html')

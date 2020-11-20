from django.shortcuts import render


def index_page(request):
    return render(request, 'app/index.html')


def profile_page(request):
    return render(request, 'app/profile.html')

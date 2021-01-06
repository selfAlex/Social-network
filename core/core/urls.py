from django.urls import path, include

from allauth.socialaccount import providers
from importlib import import_module

providers_urlpatterns = []

for provider in providers.registry.get_list():
    prov_mod = import_module(provider.get_package() + '.urls')
    providers_urlpatterns += getattr(prov_mod, 'urlpatterns', [])

urlpatterns = [

    path('', include('app.urls.urls')),

    path('handle/', include('app.urls.urls_handlers')),

    path('socialauth/', include(providers_urlpatterns)),

]

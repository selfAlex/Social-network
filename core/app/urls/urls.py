from django.urls import path

from ..views import views

urlpatterns = [

    path('', views.index_page, name='index_page'),

    path('profile', views.profile_page, name='profile_page'),
    path('profile_edit', views.profile_edit_page, name='profile_edit_page'),

    path('messenger', views.messenger_page, name='messenger_page'),

    path('api', views.api_page, name='api_page')

]

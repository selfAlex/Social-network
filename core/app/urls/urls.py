from django.urls import path

from ..views import views

urlpatterns = [

    path('', views.index_page, name='index_page'),

    path('profile', views.profile_page, name='profile_page')

]
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index_page),

    path('profile', views.profile_page)

]
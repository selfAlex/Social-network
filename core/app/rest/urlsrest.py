from django.urls import path

from . import viewsrest

urlpatterns = [

    path('user/detail/<int:pk>', viewsrest.UserDetailView.as_view()),
    path('users/list', viewsrest.UserListView.as_view()),
    path('user/create', viewsrest.UserCreateView.as_view())

]

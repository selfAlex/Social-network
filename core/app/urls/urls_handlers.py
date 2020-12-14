from django.urls import path

from ..views.views_handlers import views_handlers

urlpatterns = [

    path('signin', views_handlers.signin_handler, name='signin_handler'),
    path('signup', views_handlers.signup_handler, name='signup_handler'),

    path('verify/<str:email>/<str:password>', views_handlers.verify_user, name='verify_user'),

    path('logout', views_handlers.logout_handler, name='logout_handler')

]

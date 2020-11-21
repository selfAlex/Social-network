from django.urls import path, include

urlpatterns = [

    path('', include('app.urls.urls')),

    path('handle/', include('app.urls.urls_handlers'))

]

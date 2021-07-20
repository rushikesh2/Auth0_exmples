from django.urls import path

from . import views

urlpatterns = [
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private_scoped_shirts', views.private_scoped),
    path('api/private_scoped_trousers', views.private_scoped_trouser),
    path('api/private_scoped_shoes', views.private_scoped_shoes),
    path('api/private_scoped_collections', views.private_scoped_collections),
]

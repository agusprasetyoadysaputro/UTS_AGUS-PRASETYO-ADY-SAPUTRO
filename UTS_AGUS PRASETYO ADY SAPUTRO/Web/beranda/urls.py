from django.urls import path
from . import views

urlpatterns = [
    path('profil/', views.profil, name='profil'),
    path('add_comment/', views.add_comment, name='add_comment'),
]

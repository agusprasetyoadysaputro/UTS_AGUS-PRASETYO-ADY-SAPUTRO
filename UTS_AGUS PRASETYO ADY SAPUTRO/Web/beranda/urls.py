from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_comment/', views.add_comment, name='add_comment'),
]

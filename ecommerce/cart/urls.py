from django.urls import path

from . import views

urlpatterns = [
    path('list', views.index, name='index'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('empty', views.empty, name='empty'),
]
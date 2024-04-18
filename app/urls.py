from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_image', views.new_image, name='new_image'),
    path('teste_image', views.teste_image, name='teste_image')
]
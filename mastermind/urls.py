from django.urls import path

from . import views

app_name = 'mastermind'
urlpatterns = [
    path('', views.index, name='index'),
]

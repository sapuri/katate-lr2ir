from django.urls import path

from . import views

app_name = 'ranking'
urlpatterns = [
    path('ranking/', views.index, name='index'),
    path('ranking/<int:bms_id>/', views.bms_ranking, name='bms_ranking'),
]

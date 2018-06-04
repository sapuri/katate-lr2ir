from django.urls import path

from . import views

app_name = 'ranking'
urlpatterns = [
    path('ranking/', views.bms_list, name='bms_list'),
    path('ranking/level/<str:level>/', views.bms_list, name='bms_list'),
    path('ranking/<str:bms_id>/', views.bms_ranking, name='bms_ranking'),
]

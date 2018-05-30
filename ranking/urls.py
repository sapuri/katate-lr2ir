from django.urls import path

from . import views

app_name = 'ranking'
urlpatterns = [
    path('ranking/<str:bms_id>/', views.bms_ranking, name='bms_ranking'),
]

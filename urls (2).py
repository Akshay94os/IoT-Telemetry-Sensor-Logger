from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sensor_home'),
    path('ingest/<str:node_id>/', views.ingest_data, name='ingest_data'),
]

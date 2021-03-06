
from django.urls import path
from . import views



urlpatterns = [
    path('sightings/', views.sightings, name='sightings_list'),
    path('sightings/add', views.add_squirrel, name='add_sightings'), 
    path('sightings/stats', views.squirrel_stats, name = 'eating'),
    path('sightings/<str:Unique_Squirrel_ID>', views.edit_squirrel, name='edit_sightings'),
    
]


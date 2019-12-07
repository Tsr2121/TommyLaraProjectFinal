
from django.urls import path
from . import views



urlpatterns = [
    path('sightings/', views.sightings, name='sightings_list'),
    #path('squirrel_id', views.squirrel_id),
    path('sightings/add/', views.add_squirrel, name='add_sightings'), 
    path('sightings/<str:Unique_Squirrel_ID>', views.edit_squirrel, name='edit_sightings'),
]


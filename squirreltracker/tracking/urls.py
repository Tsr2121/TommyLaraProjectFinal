
from django.urls import path
from . import views



urlpatterns = [
    path('sightings/', views.sightings),
    #path('squirrel_id', views.squirrel_id),
    path('add/', views.add_squirrel), 
    path('<str:Unique_Squirrel_ID>/edit/', views.edit_squirrel),
]


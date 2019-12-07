
from django.urls import path
from . import views



urlpatterns = [
    path('sightings/', views.sightings),
    #path('squirrel_id', views.squirrel_id),
    #path('add/', views.add_squirrel), 
    path('<str:unique-squirrel-id>', views.edit_squirrel),
]
from django.shortcuts import render

from tracking.models import Squirrel

def map(request, *args, **kwargs):
	sightings = Squirrel.objects.all()[:50]
	context={
    'sightings':sightings
	}
	return render(request, 'map/map.html',context)

	
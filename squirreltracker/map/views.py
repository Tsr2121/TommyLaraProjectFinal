from django.shortcuts import render

from tracking.models import Squirrel

def map(request, *args, **kwargs):
	tracking = Squirrel.objects.all()[:20]
	context={
    'tracking':tracking
	}
	return render(request, 'map/map.html',context)

	
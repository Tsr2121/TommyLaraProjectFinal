from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel

def sightings(request):
	squirrels = Squirrel.objects.all()
	context = {
		'squirrels': squirrels,
	}
	return render(request, 'sightings.html', context)
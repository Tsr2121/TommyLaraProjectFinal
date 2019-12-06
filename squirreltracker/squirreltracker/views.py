from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import PetForm

def all_squirrels(request):
	squirrels = Squirrel.objects.all()
	context = {
		'squirrels': squirrels,
	}
	return render(request, 'squirreltracker/all.html', context)
from django.shortcuts import render

# Create your views here.

def sightings_list(request, squirrel_id):
	squirrels = Squirrel.objects.all()
	context = {
		'squirrels' : squirrels,
	}
	return render(request, 'tracking/all.html',  context)
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


def squirrel_id(request, Unique_Squirrel_ID ):
	squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
	return HttpResponse(squirrel.Unique_Squirrel_ID)
	#return render(request, 'squirrel_id.html')


#def add_squirrel(request):
	#if request.method == 'POST':
		#form = SquirrelForm(request.POST)
		# check data with form 
		#if form.is_valid():
			#form.save()
			#return redirect(f'/tracking/list')

	#else:
		#form = SquirrelForm()

	#context = {
		#'form': form, 
		#'jazz': True,
	#}

	#return render(request, 'tracking/edit.html', context)


def edit_squirrel(request, squirrel_id):
	squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
	if request.methof == 'POST':
		form = SquirrelForm(request.POST, instance=squirrel)

		if form.is_valid():
			form.save()
			return redirect(f'/tracking/{Unique_Squirrel_ID}')

	else:
		form = SquirrelForm(instance=squirrel)

	context = {
		'form': form, 
		'Unique_Squirrel_ID': Unique_Squirrel_ID,
	}

	return render(request, 'tracking/edit.html', context)



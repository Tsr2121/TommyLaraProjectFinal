from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel

def sightings(request,*args,**kwargs):
	squirrels = Squirrel.objects.all()
	fields = ['Unique_Squirrel_ID','Date','X', 'Y']
	context = {
		'squirrels': squirrels,
		'fields': fields,
	}
	return render(request, 'tracking/sightings.html', context)







def edit_squirrel(request, Unique_Squirrel_ID):
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



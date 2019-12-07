from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def sightings(request,*args,**kwargs):
	squirrels = Squirrel.objects.all()
	fields = ['Unique_Squirrel_ID','Date','X', 'Y']
	context = {
		'squirrels': squirrels,
		'fields': fields,
	}
	return render(request, 'tracking/sightings.html', context)



def edit_squirrel(request, Unique_Squirrel_ID):
	squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
	if request.method == 'POST':
		form = SquirrelForm(request.POST, instance=squirrel)

		if form.is_valid():
			form.save()
			return redirect(f'/tracking/{Unique_Squirrel_ID}')

	else:
		form = SquirrelForm(instance=squirrel)

	context = {
		'form': form, 

	}

	return render(request, 'tracking/edit.html', context)


def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/tracking/list/')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
        'jazz': True,
    }

    return render(request, 'tracking/edit.html', context)



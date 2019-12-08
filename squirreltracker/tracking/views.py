from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count 
from django.db.models import Max
from django.db.models import Avg

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


#def squirrel_stats(request):
	

	#return Squirrel.objects.all().aggregate(Avg('X'))


def squirrel_stats(request):
	squirrels = Squirrel.objects.all()
	
	eating_count = Squirrel.objects.values('Eating').order_by('Eating').annotate(eating_count=Count('Eating'))
	kuks_count = Squirrel.objects.values('Kuks').order_by('Kuks').annotate(kuks_count=Count('Kuks'))
	moans_count = Squirrel.objects.values('Moans').order_by('Moans').annotate(moans_count=Count('Moans'))
	chasing_count = Squirrel.objects.values('Chasing').order_by('Chasing').annotate(chasing_count=Count('Chasing'))
	running_count = Squirrel.objects.values('Running').order_by('Running').annotate(running_count=Count('Running'))
	not_eating = eating_count[0]['eating_count']
	eating = eating_count[1]['eating_count']
	not_kuks = kuks_count[0]['kuks_count']
	kuks = kuks_count[1]['kuks_count']
	not_moan = moans_count[0]['moans_count']
	moan = moans_count[1]['moans_count']
	not_chasing = chasing_count[0]['chasing_count']
	chasing = chasing_count[1]['chasing_count']
	not_running = running_count[0]['running_count']
	running = running_count[1]['running_count']


	context = {
		'eating_count': eating_count,
		'kuks_count': kuks_count,
		'moans_count': moans_count,
		'chasing_count': chasing_count,
		'running_count': running_count,
		'not_eating': not_eating,
		'eating': eating,
		'not_kuks': not_kuks,
		'kuks': kuks,
		'not_moan': not_moan,
		'moan': moan,
		'not_chasing': not_chasing,
		'chasing': chasing,
		'not_running': not_running,
		'running': running,

		
	}
	
	return render(request,'tracking/stats.html', context)





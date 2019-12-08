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
	total_num = Squirrel.objects.annotate(Count('Unique_Squirrel_ID'))

 	#eating_count = 0
 	#for i in Squirrel.objects.all():
 		#if squirrel.eating == True:
 			#eating_count +=1
 	#print ('Number of squirrels eating was', eating_count)



#def squirrel_stats(request):
	#squirrels = Squirrel.objects.all()
	context = {
		'squirrels': squirrels,
		'total_num': total_num,
	}
	#eating_stat = Squirrel.objects.values('Eating').order_by('Eating').annotate(eating_count=Count('Eating'))
	#kuks_stat = Squirrel.objects.values('Kuks').order_by('Kuks').annotate(shift_count=Count('Kuks'))
	#moans_stat = Squirrel.objects.values('Moans').order_by('Moans').annotate(moans_count=Count('Moans'))
	#chasing_stat = Squirrel.objects.values('Chasing').order_by('Chasing').annotate(chasing_count=Count('Chasing'))
	#running_stat = Squirrel.objects.values('Running').order_by('Running').annotate(running_count=Count('Running'))
	return render(request,'tracking/stats.html', context)
	#return render(request,'tracking/stats.html', context) , (eating_stat,kuks_stat,moans_stat,chasing_stat,running_stat)









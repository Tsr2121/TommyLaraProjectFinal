from django.db import models

from django.utils.translation import gettext as _

import uuid 

# Create your models here.

class Squirrel(models.Model):
	X = models.FloatField(
		help_text=_('Longitude'), 
		null=True,

	) 

	Y = models.FloatField(
		help_text=_('Latitude'), 
		null=True,
	) 

	Unique_Squirrel_ID = models.CharField(
		help_text=_('Unique_ID'),
		max_length=25, 
		#blank=True,
	)

	#AM = 'AM'
	#PM = 'PM'

	#SHIFT_CHOICES = (
	    #(AM, 'AM'),
	    #(PM, 'PM'),
	#)

	Shift = models.CharField(
		help_text=_('Shift Interval'), 
		max_length=10, 
		#choices=SHIFT_CHOICES, 
		#blank=True,
	)

	Date = models.IntegerField(
		help_text=_('Date'),
	)


	#JUVENILE = 'Juvenile'
	#ADULT = 'Adult'
	#UNRECORDED = ''


	#AGE_CHOICES = (
		#(JUVENILE, 'Juvenile'), 
		#(ADULT, 'Adult'), 
		#(UNRECORDED, ''),
	#)


	Age = models.CharField(
		help_text=_('Age Group'), 
		max_length=20, 
		#choices=AGE_CHOICES, 
		#blank=True,
	)


	#GRAY = 'Gray' 
	#CINNAMON = 'Cinnamon'
	#BLACK = 'Black'
	#UNRECORDED_COLOR = ''


	#PRIMARY_FUR_COLOR_CHOICES = (
		#(GRAY, 'Gray'), 
		#(CINNAMON, 'Cinnamon'), 
		#(BLACK, 'Black'), 
		#(UNRECORDED_COLOR, ''),
	#)

	Primary_Fur_Color = models.CharField(
		help_text=_('Primary Fur Color'), 

		max_length=25, 

		#choices=PRIMARY_FUR_COLOR_CHOICES, 
		#blank=True,
	) 


	#GROUND_PLANE = 'Ground Plane' 
	#ABOVE_GROUND = 'Above Ground'
	#UNRECORDED_LOCATION = ''


	#LOCATION_CHOICES = (
		#(GROUND_PLANE, 'Ground Plane'), 
		#(ABOVE_GROUND, 'Above Ground'), 
		#(UNRECORDED_LOCATION, ''), 
	#)

	Location = models.CharField(
		help_text=_('Location'), 
		max_length=25, 
		#choices=LOCATION_CHOICES, 
		#blank=True,
	) 


	Specific_Location = models.CharField(
		help_text=_('Specific Location'), 
		max_length=150,
		#blank=True,
	)

	TRUE = 'TRUE'
	FALSE = 'FALSE'

	Running = models.CharField(
		help_text=('Running'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Chasing = models.CharField(
		help_text=_('Chasing'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Climbing = models.CharField(
		help_text=_('Climbing'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Eating = models.CharField(
		help_text=_('Eating'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Foraging = models.CharField(
		help_text=_('Foraging'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Other_Activities = models.CharField(
		help_text=_('Other Activities'), 
		max_length=100,
		#blank=True,
	)

	Kuks = models.CharField(
		help_text=_('Kuks'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Quaas = models.CharField(
		help_text=_('Quaas'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Moans = models.CharField(
		help_text=_('Moans'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Tail_flags = models.CharField(
		help_text=_('Tail flags'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Tail_twitches = models.CharField(
		help_text=_('Tail twitches'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Approaches = models.CharField(
		help_text=_('Approaches'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Indifferent = models.CharField(
		help_text=_('Indifferent'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	Runs_from = models.CharField(
		help_text=_('Runs from'), 
		choices=((TRUE, 'TRUE'),
		(FALSE, 'FALSE')),
		default=FALSE,
		null=True,
		max_length=5,
	)

	
	





















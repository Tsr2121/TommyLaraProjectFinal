from django.db import models

from django.utils.translation import gettext as _

import uuid 

# Create your models here.

class Squirrel(models.Model):
	X = models.FloatField(
		help_text=_('Longitude'), 

	) 

	Y = models.FloatField(
		help_text=_('Latitude'), 
	) 

	Unique_Squirrel_ID = models.CharField(
		help_text=_('Unique_ID'),
		max_length=25, 
		blank=True,
	)

	AM = 'AM'
	PM = 'PM'

	SHIFT_CHOICES = (
	    (AM, 'AM'),
	    (PM, 'PM'),
	)

	Shift = models.CharField(
		help_text=_('Shift Interval'), 
		max_length=10, 
		choices=SHIFT_CHOICES, 
		blank=True,
	)

	Date = models.IntegerField(
		help_text=_('Date'),
	)


	JUVENILE = 'Juvenile'
	ADULT = 'Adult'
	UNRECORDED = ''


	AGE_CHOICES = (
		(JUVENILE, 'Juvenile'), 
		(ADULT, 'Adult'), 
		(UNRECORDED, ''),
	)


	Age = models.CharField(
		help_text=_('Age Group'), 
		max_length=20, 
		choices=AGE_CHOICES, 
		blank=True,
	)


	GRAY = 'Gray' 
	CINNAMON = 'Cinnamon'
	BLACK = 'Black'
	UNRECORDED_COLOR = ''


	PRIMARY_FUR_COLOR_CHOICES = (
		(GRAY, 'Gray'), 
		(CINNAMON, 'Cinnamon'), 
		(BLACK, 'Black'), 
		(UNRECORDED_COLOR, ''),
	)

	Primary_Fur_Color = models.CharField(
		help_text=_('Primary Fur Color'), 
		max_length=10, 
		choices=PRIMARY_FUR_COLOR_CHOICES, 
		blank=True,
	) 


	GROUND_PLANE = 'Ground Plane' 
	ABOVE_GROUND = 'Above Ground'
	UNRECORDED_LOCATION = ''


	LOCATION_CHOICES = (
		(GROUND_PLANE, 'Ground Plane'), 
		(ABOVE_GROUND, 'Above Ground'), 
		(UNRECORDED_LOCATION, ''), 
	)

	Location = models.CharField(
		help_text=_('Location'), 
		max_length=25, 
		choices=LOCATION_CHOICES, 
		blank=True,
	) 


	Specific_Location = models.CharField(
		help_text=_('Specific Location'), 
		max_length=150,
		blank=True,
	)

	Running = models.BooleanField(
		help_text=_('Running'), 
		default=True,
	)

	Chasing = models.BooleanField(
		help_text=_('Chasing'), 
		default=True,
	)

	Climbing = models.BooleanField(
		help_text=_('Climbing'), 
		default=True,
	)

	Eating = models.BooleanField(
		help_text=_('Eating'), 
		default=True,
	)

	Foraging = models.BooleanField(
		help_text=_('Foraging'), 
		default=True,
	)

	Other_Activities = models.CharField(
		help_text=_('Other Activities'), 
		max_length=100,
		blank=True,
	)

	Kuks = models.BooleanField(
		help_text=_('Kuks'), 
		default=True,
	)

	Quaas = models.BooleanField(
		help_text=_('Quaas'), 
		default=True,
	)

	Moans = models.BooleanField(
		help_text=_('Moans'), 
		default=True,
	)

	Tail_flags = models.BooleanField(
		help_text=_('Tail flags'), 
		default=True,
	)

	Tail_twitches = models.BooleanField(
		help_text=_('Tail twitches'), 
		default=True,
	)

	Approaches = models.BooleanField(
		help_text=_('Approaches'), 
		default=True,
	)

	Indifferent = models.BooleanField(
		help_text=_('Indifferent'), 
		default=True,
	)

	Runs_from = models.BooleanField(
		help_text=_('Runs from'), 
		default=True,
	)

	
	





















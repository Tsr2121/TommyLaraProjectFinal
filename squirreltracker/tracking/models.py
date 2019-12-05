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

	Unique_Squirrel_ID = models.UUIDField(
		id = models.UUIDField(primary_key=True), 
		help_text=_('Unique_ID'),
	)

	Hectare = models.CharField(
		help_text=_('Hectare'), 
		max_length=10,
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
	)

	Date = models.DateField(
		help_text=_('Date'),
	)

	Hectare_Squirrel_Number = models.PositiveIntegerField(
		help_text=_('Hectare Squirrel Number'),
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
	) 


	Highlight_Fur_Color = models.CharField(
		help_text=_('Highlight Fur Color'), 
		max_length=20,
	)

	Combination_of_Primary_and_Highlight_Color = models.CharField(
		help_text=_('Primary and Highlight Color'), 
		max_length=20, 
	)

	Color_Notes = models.CharField(
		help_text=_('Color Notes'), 
		max_length=150,
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
	) 

	Above_Ground_Sighter_Measurement = models.PositiveIntegerField(

	)

	Specific_Location = models.CharField(
		help_text=_('Specific Location'), 
		max_length=150,
	)

	Running = models.BooleanField(
		help_text=_('Running'), 
	)

	Chasing = models.BooleanField(
		help_text=_('Chasing'), 
	)

	Climbing = models.BooleanField(
		help_text=_('Climbing'), 
	)

	Eating = models.BooleanField(
		help_text=_('Eating'), 
	)

	Foraging = models.BooleanField(
		help_text=_('Foraging'), 
	)

	Other_Activities = models.CharField(
		help_text=_('Other Activities'), 
		max_length=100,
	)

	Kuks = models.BooleanField(
		help_text=_('Kuks'), 
	)

	Quaas = models.BooleanField(
		help_text=_('Quaas'), 
	)

	Moans = models.BooleanField(
		help_text=_('Moans'), 
	)

	Tail_flags = models.BooleanField(
		help_text=_('Tail flags'), 
	)

	Tail_twitches = models.BooleanField(
		help_text=_('Tail twitches'), 
	)

	Approaches = models.BooleanField(
		help_text=_('Approaches'), 
	)

	Indifferent = models.BooleanField(
		help_text=_('Indifferent'), 
	)

	Runs_from = models.BooleanField(
		help_text=_('Runs from'), 
	)

	Approaches = models.BooleanField(
		help_text=_('Approaches'), 
	)

	Other_Interactions = models.CharField(
		help_text=_('Other Interactions'), 
		max_length=100,
	)

	Lat_Long = models.CharField(
		help_text=_('Lat Long'), 
		max_length=100,
	)


	Zip_Codes = models.PositiveIntegerField(
		help_text=_('Zip Codes'),
	)

	Community_Districts = models.PositiveIntegerField(
		help_text=_('Community Districts'),
	)

	Borough_Boundaries = models.PositiveIntegerField(
		help_text=_('Borough_Boundaries'),
	)

	City_Council_Districts = models.PositiveIntegerField(
		help_text=_('City Council Districts'),
	)

	Police_Precincts = models.PositiveIntegerField(
		help_text=_('Police Precincts'),
	)

	def __str__(self):
        return self.name
























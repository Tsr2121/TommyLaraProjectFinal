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
		max_length=10
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
		help_text=_('Date')
		)

	Hectare_Squirrel_Number = models.PositiveIntegerField(
		help_text=_('Hectare Squirrel Number')
		)

	JUVENILE = 'Juvenile'
	ADULT = 'Adult'
	UNRECORDED = ''


	AGE_CHOICES = (
		(JUVENILE, 'Juvenile'), 
		(ADULT = 'Adult'), 
		(UNRECORDED = ''),
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
		(GRAY = 'Gray'), 
		(CINNAMON = 'Cinnamon'), 
		(BLACK = 'Black'), 
		(UNRECORDED_COLOR = ''),
		)

	Primary_Fur_Color = models.CharField(
		help_text=_('Primary Fur Color'), 
		max_length=10, 
		choices=PRIMARY_FUR_COLOR_CHOICES, 
		) 


	Highlight_Fur_Color = models.CharField(
		help_text=_('Highlight Fur Color'), 
		max_length=20
		)

	Combination_of_Primary_and_Highlight_Color = models.CharField(
		help_text=_('Primary and Highlight Color'), 
		max_length=20 
		)

	Color_Notes = models.CharField(
		help_text=_('Color Notes'), 
		max_length=150
		)

	GROUND_PLANE = 'Ground Plane' 
	ABOVE_GROUND = 'Above Ground'
	UNRECORDED_LOCATION = ''


	LOCATION_CHOICES = (
		(GROUND_PLANE = 'Ground Plane'), 
		(ABOVE_GROUND = 'Above Ground'), 
		(UNRECORDED_LOCATION = ''), 
		)

	Location = models.CharField(
		help_text=_('Location'), 
		max_length=25, 
		choices=LOCATION_CHOICES, 
		) 












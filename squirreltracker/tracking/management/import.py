import csv

from django.core.management.base import BaseCommand

from tracking.models import Squirrels


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            p = Squirrels(
                X=item['X'],
                Y=item['Y'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Hectare=item['Hectare'],
                Shift = item['Shift'], 
                Date = item['Date'], 
                Hectare_Squirrel_Number = item['Hectare Squirrel Number'], 
                Age = item['Age'], 
                Primary_Fur_Color = item['Primary Fur Color'], 
                Highlight_Fur_Color = item['Highlight Fur Color'], 
                Combination_of_Primary_and_Highlight_Color = item['Combination of Primary and Highlight Color'],
                Color_notes = item['Color notes'], 
                Location = item['Location'], 
                Above_Ground_Sighter_Measurement = item['Above Ground Sighter Measurement'], 
                Specific_Location = item['Specific Location'], 
                Running = item['Running'], 
                Chasing = item['Chasing'], 
                Climbing = item['Climbing'], 
                Eating = item['Eating'], 
                Foraging = item['Foraging'], 
                Other_Activities = item['Other Activities'], 
                Kuks = item['Kuks'], 
                Quaas = item['Quaas'], 
                Moans = item['Moans'], 
                Tail_flags = item['Tail flags'], 
                Tail_twitches = item['Tail twitches'], 
                Approaches = item['Approaches'], 
                Indifferent = item['Indifferent'], 
                Runs_from = item['Runs from'], 
                Other_Interactions = item['Other Interactions'],
                Lat_Long = item['Lat/Long'], 
                Zip_Codes = item['Zip Codes'], 
                Community_Districts = item['Community Districts'], 
                Borough_Boundaries = item['Borough Boundaries'], 
                City_Council_Districts = item['City Council Districts'], 
                Police_Precincts = item['Police Precincts']
            )
            p.save()

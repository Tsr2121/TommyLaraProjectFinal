import csv

from django.core.management.base import BaseCommand

from tracking.models import Squirrel

import pandas as pd 


class Command(BaseCommand):
    help = 'export fields'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            writer = csv.writer(fp)
            data = list(reader)

        for item in data:
            p = Squirrel(
                X=item['X'],
                Y=item['Y'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Shift = item['Shift'], 
                Date = item['Date'], 
                Age = item['Age'], 
                Primary_Fur_Color = item['Primary Fur Color'], 
                Location = item['Location'],  
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
            )
            p.to_csv(csv_file)
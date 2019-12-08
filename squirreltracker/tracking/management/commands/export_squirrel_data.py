
import csv
import sys

from django.core.management.base import BaseCommand, CommandError

from tracking.models import Squirrel



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        meta = Squirrel._meta
        fields = [j.name for j in meta.fields]
        csv_file = options['csv_file']
        
        print(csv_file)
        with open(csv_file,'w') as csvfile:
            w = csv.writer(csvfile)

            w.writerow(fields)
            for i in Squirrel.objects.all():
                w.writerow([getattr(i, field) for field in fields])


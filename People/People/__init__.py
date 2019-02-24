import csv
import os
from .constants import data_filename
from .database import Person, persons
from django.conf import settings

filename = data_filename
# get absolute path for file
path = os.path.join(settings.BASE_DIR, filename)

with open(path) as file:
    reader = csv.DictReader(file)  # read rows into a dictionary format
    for row in reader:
        person = Person(first_name=row['givenName'],
                        middle_name=row['middleName'],
                        last_name=row['surname'])
        persons.append(person)

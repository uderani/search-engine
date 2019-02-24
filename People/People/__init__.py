import csv
import os
from .constants import data_filename
from .database import Person, persons
from django.conf import settings

"""
Initialization code which imports data from the csv and adds it 
to the server database which is list in this case so as to not use any libraries 
"""
filename = data_filename
# get absolute path for file
path = os.path.join(settings.BASE_DIR, filename)

with open(path) as file:
    reader = csv.DictReader(file)  # read rows into a dictionary format
    count = 0
    # iterate through csv rows using dictionary
    for row in reader:
        person = Person(first_name=row['givenName'],
                        middle_name=row['middleName'],
                        last_name=row['surname'],
                        index=count)

        # Create tuples in database and also index them with each insertion
        persons.append(person)
        count += 1



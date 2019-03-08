#Extracting Text to New Features
'''
Garages are an important consideration for houses in Minnesota where most people own a car and the snow is annoying to clear off a car parked outside. The type of garage is also important, can you get to your car without braving the cold or not? Let's look at creating a feature has_attached_garage that captures whether the garage is attached to the house or not.

Instructions
100 XP

Import the needed function when() from pyspark.sql.functions.
Create a string matching condition using like() to look for for the string pattern Attached Garage in df['GARAGEDESCRIPTION'] and use wildcards % so it will match anywhere in the field.
Similarly, create another condition using like() to find the string pattern Detached Garage in df['GARAGEDESCRIPTION'] and use wildcards % so it will match anywhere in the field.
Create a new column has_attached_garage using when() to assign the value 1 if it has an attached garage, zero if detached and use otherwise() to assign null with None if it is neither.
'''

# Code
# Import needed functions
from pyspark.sql.functions import when

# Create boolean conditions for string matches
has_attached_garage = df['GARAGEDESCRIPTION'].like('%Attached Garage%')
has_detached_garage = df['GARAGEDESCRIPTION'].like('%Detached Garage%')

# Conditional value assignment 
df = df.withColumn('has_attached_garage', (when(has_attached_garage, 1)
                                          .when(has_detached_garage, 0)
                                          .otherwise(None)))

# Inspect results
df[['GARAGEDESCRIPTION', 'has_attached_garage']].show(truncate=100)

'''result
<script.py> output:
    +------------------------------------------------------------------+-------------------+
    |                                                 GARAGEDESCRIPTION|has_attached_garage|
    +------------------------------------------------------------------+-------------------+
    |                                                   Attached Garage|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |                                                   Attached Garage|                  1|
    |    Attached Garage, Detached Garage, Tuckunder, Driveway - Gravel|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |                               Attached Garage, Driveway - Asphalt|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |                                                   Attached Garage|                  1|
    |                                                   Attached Garage|                  1|
    |                                                   Attached Garage|                  1|
    |                                                   Attached Garage|                  1|
    |                                                   Attached Garage|                  1|
    |                                                   Attached Garage|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |Attached Garage, Tuckunder, Driveway - Asphalt, Garage Door Opener|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    |           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|
    +------------------------------------------------------------------+-------------------+
    only showing top 20 rows

'''
#Splitting & Exploding
'''
Being able to take a compound field like GARAGEDESCRIPTION and massaging it into something useful is an involved process. It's helpful to understand early what value you might gain out of expanding it. In this example, we will convert our string to a list-like array, explode it and then inspect the unique values.

Instructions
100 XP
Import the needed functions split() and explode() from pyspark.sql.functions
Use split() to create a new column garage_list by splitting df['GARAGEDESCRIPTION'] on ', ' which is both a comma and a space.
Create a new record for each value in the df['garage_list'] using explode() and assign it a new column ex_garage_list
Use distinct() to get unique values of ex_garage_list and show the 100 first rows, truncating them at 50 characters to display the values.
'''

# Code
# Import needed functions
from pyspark.sql.functions import split,explode

# Convert string to list-like array
df = df.withColumn('garage_list', split(df['GARAGEDESCRIPTION'], ', '))

# Explode the values into new records
ex_df = df.withColumn('ex_garage_list', explode(df['garage_list']))

# Inspect the values
ex_df[['ex_garage_list']].distinct().show(100, truncate=50)

'''result
<script.py> output:
    +----------------------------+
    |              ex_garage_list|
    +----------------------------+
    |             Attached Garage|
    |      On-Street Parking Only|
    |                        None|
    | More Parking Onsite for Fee|
    |          Garage Door Opener|
    |   No Int Access to Dwelling|
    |           Driveway - Gravel|
    |       Valet Parking for Fee|
    |              Uncovered/Open|
    |               Heated Garage|
    |          Underground Garage|
    |                       Other|
    |                  Unassigned|
    |More Parking Offsite for Fee|
    |    Driveway - Other Surface|
    |       Contract Pkg Required|
    |                     Carport|
    |                     Secured|
    |             Detached Garage|
    |          Driveway - Asphalt|
    |                  Units Vary|
    |                    Assigned|
    |                   Tuckunder|
    |                     Covered|
    |            Insulated Garage|
    |         Driveway - Concrete|
    |                      Tandem|
    |           Driveway - Shared|
    +----------------------------+

'''
#Grouped summary statistics
'''
In this exercise, we are going to combine the .groupBy() and .filter() methods that you've used previously to calculate the min and avg number of users that have rated each song, and the minand avg number of songs that each user has rated. Because our data now includes 0's for items not yet consumed, we'll need to .filter() them out when doing grouped summary statistics like this. The msd dataset is provided for you here.

Instructions
100 XP

The col, minand avg fucntions from pyspark.sql.functions have been imported for you.
As an example, the .filter(), .groupBy() and .count() methods are applied to the msd dataset along with the select() and min methods to return the smallest number of ratings that any song in the dataset has received. Use this as a model to calculate the avg number of implicit ratings the songs in msd have received.
Using the same model, find the min and avg number of implicit ratings that userId's have provided in the msd dataset.
'''

# Code
# Min num implicit ratings for a song
print("Most implicit ratings for a song: ")
msd.filter(col("num_plays") > 0).groupBy("songId").count().select(min("count")).show()

# Avg num implicit ratings per songs
print("Avg num implicit ratings per song: ")
msd.filter(col("num_plays") > 0).groupBy("songId").count().select(avg("count")).show()

# Min num implicit ratings from a user
print("Fewest implicit ratings from a user: ")
msd.filter(col("num_plays") > 0).groupBy("userId").count().select(min("count")).show()

# Avg num implicit ratings for users
print("Avg num implicit ratings per user: ")
msd.filter(col("num_plays") > 0).groupBy("userId").count().select(avg("count")).show()

'''result
<script.py> output:
    Most implicit ratings for a song: 
    +----------+
    |min(count)|
    +----------+
    |         3|
    +----------+
    
    Avg num implicit ratings per song: 
    +------------------+
    |        avg(count)|
    +------------------+
    |35.251063829787235|
    +------------------+
    
    Fewest implicit ratings from a user: 
    +----------+
    |min(count)|
    +----------+
    |        21|
    +----------+
    
    Avg num implicit ratings per user: 
    +-----------------+
    |       avg(count)|
    +-----------------+
    |77.42056074766356|
    +-----------------+
'''
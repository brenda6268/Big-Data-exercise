#MovieLens Summary Statistics
'''
Let's take the groupBy() method a bit firther. Once you've applied the .groupBy() method to a dataframe, you can subsequently run aggregate functions such as .sum(), .avg(), .min() and have the results grouped. This exercise will walk you through how this is done. The min and avg functions have been imported from pyspark.sql.functions for you.

Instructions
100 XP

Group the data by movieId and use the .count() method to calculate how many ratings each movie has received. From this, call the .select() method to select the following metrics:
min("count") to get the smallest number of ratings that any movie in the dataset. This first one is given to you as an example.
avg("count") to get the average number of ratings per movie
Do the same thing, but this time group by userId to get the min and avg number of ratings.
'''

# code
# Min num ratings for movies
print("Movie with the fewest ratings: ")
ratings.groupBy("movieId").count().select(min("count")).show()

# Avg num ratings per movie
print("Avg num ratings per movie: ")
ratings.groupBy("movieId").count().select(avg("count")).show()

# Min num ratings for user
print("User with the fewest ratings: ")
ratings.groupBy("userId").count().select(min("count")).show()

# Avg num ratings per users
print("Avg num ratings per user: ")
ratings.groupBy("userId").count().select(avg("count")).show()

'''
Movie with the fewest ratings: 
+----------+
|min(count)|
+----------+
|         1|
+----------+

Avg num ratings per movie: 
+------------------+
|        avg(count)|
+------------------+
|11.030664019413193|
+------------------+

User with the fewest ratings: 
+----------+
|min(count)|
+----------+
|        20|
+----------+

Avg num ratings per user: 
+------------------+
|        avg(count)|
+------------------+
|149.03725782414307|
+------------------+
'''
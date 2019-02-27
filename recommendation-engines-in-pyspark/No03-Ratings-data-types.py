#Ratings data types
'''
Markus watches a lot of movies, from documentaries to superhero movies, classics and dramas. Drawing on your previous experience with Spark, use the markus_ratings dataframe, which contains data on the number of movie views Markus has seen in various genres, think about whether these are implicit or explicit ratings, and use the groupBy() method to determine which genre has the highest rating, which could likely influence what recommendations ALS would generate for Markus.

Instructions
100 XP

Use the groupBy() method to group the markus_ratings dataframe by "Genre".
Apply the .sum() method to get the total number of movies watched for each genre.
Be sure to add the .show() method at the end to view the counts.
'''

# Code
# Group the data by "Genre"
markus_ratings.groupBy("Genre").sum().show()

'''
+------------------+--------------+
|             Genre|sum(Num_Views)|
+------------------+--------------+
|             Drama|             5|
|       Documentary|             3|
|            Action|             4|
|Animated Childrens|            49|
+------------------+--------------+
'''
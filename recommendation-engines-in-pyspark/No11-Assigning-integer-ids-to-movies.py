#Assigning integer id's to movies
'''
Let's now do the same thing to the movies. Then let's join the new user id's and movie id's into one dataframe.

Instructions
100 XP
Use the .select() and the .distinct() methods to extract all unique Movie's from the ratings dataframe.
Repartition the movies dataframe to one partition using the coalesce() method.
Complete the partial code provided to assign unique integer id's to each movie. Name the new column movieId and call the .persist() method on the resulting dataframe.
Join the ratings dataframe to the users dataframe and subsequently to the movies dataframe. Call the result movie_ratings.
'''

# Code
# Extract the distinct movie id's
movies = ratings.select("Movie").distinct() 

# Repartition the data to have only one partition.
movies = movies.coalesce(1) 

# Create a new column of movieId integers. 
movies = movies.withColumn("movieId", monotonically_increasing_id()).persist() 

# Join the ratings, users and movies dataframes
movie_ratings = ratings.join(users, "User", "left").join(movies, "Movie", "left")
movie_ratings.show()

'''result

+----------+----------------+------+------+-------+
|     Movie|            User|Rating|userId|movieId|
+----------+----------------+------+------+-------+
|     Shrek|    James Alking|     3|     2|      3|
|      Coco|    James Alking|     4|     2|      1|
|Swing Kids|    James Alking|     4|     2|      2|
|  Sneakers|    James Alking|     3|     2|      0|
|     Shrek|Elvira Marroquin|     4|     0|      3|
|      Coco|Elvira Marroquin|     5|     0|      1|
|  Sneakers|Elvira Marroquin|     2|     0|      0|
|      Coco|      Jack Bauer|     2|     1|      1|
|Swing Kids|      Jack Bauer|     2|     1|      2|
|  Sneakers|      Jack Bauer|     5|     1|      0|
|     Shrek|     Julia James|     5|     3|      3|
|Swing Kids|     Julia James|     2|     3|      2|
|  Sneakers|     Julia James|     2|     3|      0|
+----------+----------------+------+------+-------+
'''